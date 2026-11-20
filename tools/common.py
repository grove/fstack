"""Small offline helpers for authoring and packaging standalone methods."""
from __future__ import annotations

import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 2 * 1024 * 1024
NAME = re.compile(r'fstack-[a-z0-9]+(?:-[a-z0-9]+)*\Z')
GROUPS = {'understanding', 'design', 'implementation', 'verification', 'collaboration', 'improvement'}
HEADINGS = ('Starting point', 'Method', 'What to return', 'Boundaries', 'Worked example')


def read_bytes(path):
    """Reject devices, pipes, symbolic links and unbounded input reads."""
    path = Path(path)
    if path.is_symlink():
        raise ValueError(f'Symbolic-link input is not supported: {path}')
    flags = os.O_RDONLY | getattr(os, 'O_NONBLOCK', 0) | getattr(os, 'O_NOFOLLOW', 0)
    descriptor = os.open(path, flags)
    with os.fdopen(descriptor, 'rb') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise ValueError(f'Expected a regular file: {path}')
        if info.st_size > MAX_BYTES:
            raise ValueError(f'Input exceeds {MAX_BYTES} bytes: {path}')
        data = stream.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError(f'Input exceeds {MAX_BYTES} bytes: {path}')
        return data


def read_text(path):
    return read_bytes(path).decode('utf-8')


def load_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f'Duplicate JSON key: {key}')
            result[key] = value
        return result

    def invalid_constant(value):
        raise ValueError(f'Invalid JSON constant: {value}')

    return json.loads(read_text(path), object_pairs_hook=pairs, parse_constant=invalid_constant)


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def frontmatter(text):
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('Missing YAML frontmatter.')
    header = text[4:].split('\n---\n', 1)[0]
    fields = {}
    for line in header.splitlines():
        if ': ' not in line:
            raise ValueError('Use canonical single-line name and description fields.')
        key, value = line.split(': ', 1)
        if key in fields:
            raise ValueError(f'Duplicate frontmatter field: {key}')
        if key == 'description':
            if not value.startswith('"'):
                raise ValueError('Use a JSON-quoted description scalar, which is also valid YAML.')
            value = json.loads(value)
        fields[key] = value
    if set(fields) != {'name', 'description'}:
        raise ValueError('Use only name and description in skill frontmatter.')
    if not isinstance(fields['name'], str) or not NAME.fullmatch(fields['name']) or len(fields['name']) > 64:
        raise ValueError('Invalid fstack skill name.')
    if not nonempty_text(fields['description']) or len(fields['description']) > 1024:
        raise ValueError('Description must contain 1-1024 characters.')
    if any(c in fields['description'] for c in '<>'):
        raise ValueError('Description must not contain angle brackets.')
    return fields


def catalog(root=ROOT):
    data = load_json(root / 'catalog.json')
    if not isinstance(data, dict) or set(data) != {'version', 'skills'}:
        raise ValueError('Catalog requires version and skills only.')
    if not isinstance(data['version'], str) or not re.fullmatch(r'\d+\.\d+\.\d+', data['version']):
        raise ValueError('Invalid catalog version.')
    if not isinstance(data['skills'], list) or not data['skills']:
        raise ValueError('Catalog must contain skills.')
    result = {}
    for item in data['skills']:
        if not isinstance(item, dict) or set(item) != {'name', 'group', 'purpose'}:
            raise ValueError('Catalog entry requires name, group and purpose only.')
        name = item['name']
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            raise ValueError(f'Invalid catalog name: {name!r}')
        if name in result:
            raise ValueError(f'Duplicate skill: {name}')
        if not isinstance(item['group'], str) or item['group'] not in GROUPS or not nonempty_text(item['purpose']):
            raise ValueError(f'Invalid group or purpose for {name}.')
        result[name] = item
    return result


def relative_path(value):
    if (not isinstance(value, str) or not value or '\\' in value or ':' in value
            or any(ord(c) < 32 for c in value)):
        raise ValueError(f'Invalid relative path: {value!r}')
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {'', '.', '..', '.git'} for part in value.split('/')):
        raise ValueError(f'Unsafe relative path: {value!r}')
    return path


def package_files(name, root=ROOT):
    if name not in catalog(root):
        raise ValueError(f'Unknown skill: {name}')
    source = root / 'skills' / name
    if source.is_symlink() or not source.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Symbolic-link skill directory: {name}')
    text = read_text(source / 'SKILL.md')
    if frontmatter(text)['name'] != name:
        raise ValueError(f'Skill directory and frontmatter name disagree: {name}')
    result = {}
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolic-link package resource: {path}')
        if path.is_dir():
            continue
        relative = path.relative_to(source).as_posix()
        relative_path(relative)
        result[relative] = read_bytes(path)
        if path.suffix == '.md':
            errors = link_errors(path, source)
            if errors:
                raise ValueError('; '.join(errors))
    return result


def link_errors(path, boundary):
    text = re.sub(r'```.*?```', '', read_text(path), flags=re.S)
    errors = []
    for raw in re.findall(r'\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)', text):
        target = raw.split('#', 1)[0]
        if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
            continue
        candidate = (path.parent / unquote(target)).resolve()
        if not candidate.is_relative_to(boundary.resolve()) or not candidate.exists():
            errors.append(f'{path}: broken or non-contained resource link {raw}')
    return errors


def validate_case(case, known):
    required = {'id', 'skill', 'task', 'context', 'expected', 'forbidden', 'evidence', 'mode'}
    if not isinstance(case, dict) or not required.issubset(case) or set(case) - required - {'fixtures'}:
        raise ValueError('Evaluation case has missing or unknown fields.')
    if not isinstance(case['skill'], str) or case['skill'] not in known or case['id'] != case['skill']:
        raise ValueError('Case identity must name its catalog skill.')
    for key in ('task', 'context'):
        if not nonempty_text(case[key]):
            raise ValueError(f'Case {key} must be nonempty text.')
    for key in ('expected', 'forbidden', 'evidence'):
        values = case[key]
        if not isinstance(values, list) or not values or not all(nonempty_text(v) for v in values):
            raise ValueError(f'Case {key} must be a nonempty list of strings.')
        if len(values) != len(set(values)):
            raise ValueError(f'Case {key} repeats a criterion.')
    if case['mode'] not in ('reasoning', 'workspace'):
        raise ValueError('Case mode must be reasoning or workspace.')
    fixtures = case.get('fixtures', [])
    if not isinstance(fixtures, list) or (case['mode'] == 'workspace' and not fixtures):
        raise ValueError('Workspace cases require a nonempty fixture list.')
    if case['mode'] == 'reasoning' and fixtures:
        raise ValueError('Reasoning cases must put supplied records in context, not fixture files.')
    paths = set()
    for fixture in fixtures:
        if not isinstance(fixture, dict) or set(fixture) != {'path', 'content'} or not isinstance(fixture['content'], str):
            raise ValueError('Fixture requires a path and UTF-8 content string.')
        path = relative_path(fixture['path'])
        if str(path).casefold() in paths:
            raise ValueError(f'Duplicate or case-colliding fixture path: {path}')
        paths.add(str(path).casefold())
    for path in paths:
        if any(str(parent) in paths for parent in PurePosixPath(path).parents if str(parent) != '.'):
            raise ValueError(f'Fixture file/directory collision: {path}')
    return case


def write_bundle(output, files, root=ROOT):
    """Create a new/empty destination atomically after validating every source."""
    output = Path(output).absolute()
    for part in (output, *output.parents):
        if part.is_symlink():
            raise ValueError('Output must not traverse symbolic links.')
    output = output.resolve()
    protected = [root / p for p in ('.git', '.github', 'skills', 'tools', 'tests', 'docs',
                                    'evals', 'examples', 'principles', 'recipes')]
    if output == root.resolve() or any(output.is_relative_to(p.resolve()) for p in protected):
        raise ValueError('Output must not overlap library source directories; use dist or a separate workspace.')
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError('Output must be absent or an empty directory.')
    for path, data in files.items():
        relative_path(path)
        if not isinstance(data, bytes):
            raise ValueError('Bundle contents must be bytes.')
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.fstack-stage-', dir=output.parent))
    try:
        for path, data in files.items():
            target = staging / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        # Recheck immediately before replacement; never replace a populated directory.
        if output.is_symlink() or (output.exists() and (not output.is_dir() or any(output.iterdir()))):
            raise ValueError('Output changed while preparing the bundle.')
        os.replace(staging, output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def data_block(text):
    longest = max((len(m.group()) for m in re.finditer(r'`+', text)), default=0)
    fence = '`' * max(3, longest + 1)
    return f'{fence}text\n{text}\n{fence}'
