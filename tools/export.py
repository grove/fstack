#!/usr/bin/env python3
"""Export complete standalone skill packages. Does not install or call an agent."""
import argparse
from pathlib import Path

from common import ROOT, catalog, package_files, read_bytes, write_bundle


def export(output, selected=None, root=ROOT):
    known = catalog(root)
    selected = sorted(known) if selected is None else selected
    if not selected or len(selected) != len(set(selected)):
        raise ValueError('Select each skill once; an empty selection is invalid.')
    if set(selected) - set(known):
        raise ValueError('Unknown skill selection: ' + ', '.join(sorted(set(selected) - set(known))))
    files = {}
    license_bytes = read_bytes(root / 'LICENSE')
    for name in selected:
        for path, content in package_files(name, root).items():
            files[f'{name}/{path}'] = content
        files[f'{name}/LICENSE'] = license_bytes
    write_bundle(output, files, root)
    return len(selected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--skill', action='append')
    args = parser.parse_args()
    try:
        count = export(args.output, args.skill)
        print(f'Exported {count} standalone skills to {args.output}.')
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')
