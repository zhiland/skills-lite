#!/usr/bin/env python3
"""Copy one repository skill without replacing an existing installation."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def install(source: Path, destination: Path) -> Path:
    source = source.absolute()
    allowed = [ROOT / group / 'skills' for group in ('openspec', 'matt-pocock-skills')]
    if source.is_symlink() or source.resolve().parent not in allowed:
        raise ValueError('Select a skill directory from this repository.')
    source = source.resolve()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('The source has no SKILL.md.')
    if any(p.is_symlink() for p in source.rglob('*')):
        raise ValueError('Skill files must not contain symbolic links.')
    target = destination.expanduser() / source.name
    # lexists semantics also reject a dangling symlink at the target.
    if target.exists() or target.is_symlink():
        raise FileExistsError(f'Preserving existing destination: {target}')
    destination.expanduser().mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)  # Also refuses collisions created after the check.
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--dest', required=True, type=Path)
    args = parser.parse_args()
    try:
        print(install(args.source, args.dest))
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
