#!/usr/bin/env python3
"""Validate standalone skills, catalog coverage, evaluation cases and local links."""
from pathlib import Path
import re
import sys
from common import ROOT, HEADINGS, catalog, link_errors, load_json, package_files, read_text, validate_case


def validate(root=ROOT):
    errors = []
    try:
        known = catalog(root)
    except (ValueError, OSError) as exc:
        return [str(exc)], {}
    directories = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if directories != set(known):
        errors.append('Skill directories and catalog disagree.')
    for name in known:
        try:
            source = root / 'skills' / name
            package_files(name, root)
            text = read_text(source / 'SKILL.md')
            if len(text.splitlines()) >= 500:
                errors.append(f'{name}: skill must remain below 500 lines.')
            headings = re.findall(r'^## (.+)$', text, re.M)
            if headings != list(HEADINGS):
                errors.append(f'{name}: use the five canonical method sections in order.')
            for heading in HEADINGS:
                marker = '## ' + heading + '\n'
                if marker in text and not text.split(marker, 1)[1].split('\n## ', 1)[0].strip():
                    errors.append(f'{name}: empty {heading} section.')
            if re.search(r'\[(?:TODO|TBD|FIXME)\b|lorem ipsum', text, re.I):
                errors.append(f'{name}: unfinished authoring placeholder.')
            for file in source.rglob('*.md'):
                errors.extend(link_errors(file, source))
        except (ValueError, OSError) as exc:
            errors.append(f'{name}: {exc}')
    cases = sorted((root / 'evals/cases').glob('*.json'))
    if {p.stem for p in cases} != set(known):
        errors.append('Every skill needs exactly one matching evaluation case.')
    for path in cases:
        try:
            case = validate_case(load_json(path), known)
            if path.stem != case['id']:
                errors.append(f'{path}: filename and case identity disagree.')
        except (ValueError, OSError) as exc:
            errors.append(f'{path}: {exc}')
    for path in root.rglob('*.md'):
        parts = path.relative_to(root).parts
        if any(p in {'.git', '.venv', 'dist', 'skills'} for p in parts):
            continue
        errors.extend(link_errors(path, root))
    for quadrant in ('tutorials', 'how-to', 'reference', 'explanation'):
        if not list((root / 'docs' / quadrant).glob('*.md')):
            errors.append(f'Missing Diataxis documentation quadrant: {quadrant}.')
    reference = root / 'docs/reference/catalog.md'
    if reference.exists():
        text = read_text(reference)
        for name in known:
            if name not in text:
                errors.append(f'Catalog documentation omits {name}.')
    return errors, {'skills': len(known), 'cases': len(cases)}


if __name__ == '__main__':
    errors, counts = validate()
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Validation passed: {counts['skills']} standalone skills and {counts['cases']} evaluation cases.")
