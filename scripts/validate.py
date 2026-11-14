#!/usr/bin/env python3
"""Validate this collection's portable metadata and local file references."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    skills = sorted(root.glob('*/skills/*/SKILL.md'))
    names = set()
    if len(skills) != 8:
        errors.append(f'Expected 8 skills, found {len(skills)}')
    for path in skills:
        relative = path.relative_to(root)
        text = path.read_text()
        try:
            parts = text.split('---\n', 2)
            if len(parts) != 3 or parts[0]:
                raise ValueError('missing frontmatter')
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                raise ValueError('frontmatter must be a mapping')
            name = meta.get('name', '')
            if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
                raise ValueError('invalid name')
            if name != path.parent.name or name in names:
                raise ValueError('duplicate name or folder/name mismatch')
            names.add(name)
            description = meta.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                raise ValueError('invalid description')
            if set(meta) - {'name', 'description', 'disable-model-invocation', 'argument-hint'}:
                raise ValueError('unexpected frontmatter keys')
            if 'argument-hint' in meta and not isinstance(meta['argument-hint'], str):
                raise ValueError('argument-hint must be a string')
            if meta.get('disable-model-invocation') is not True:
                raise ValueError('Claude manual invocation flag missing')
            if not parts[2].strip() or '[TODO:' in parts[2]:
                raise ValueError('empty or unfinished body')
        except (ValueError, OSError, yaml.YAMLError) as error:
            errors.append(f'{relative}: {error}')
    for path in root.rglob('*.md'):
        if '.git' in path.parts or '.venv' in path.parts:
            continue
        text = path.read_text()
        if '/Users/' in text or '/private/tmp/' in text:
            errors.append(f'{path.relative_to(root)}: private machine path')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'^[a-z]+:', link) or link.startswith('#'):
                continue
            target = (path.parent / unquote(link.split('#')[0])).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'{path.relative_to(root)}: invalid local link {link}')
    for path in root.rglob('*'):
        if '.git' in path.parts or '.venv' in path.parts:
            continue
        if path.is_symlink():
            errors.append(f'{path.relative_to(root)}: unexpected symbolic link')
    return skills, errors


if __name__ == '__main__':
    skills, errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    total = sum(p.stat().st_size for p in skills)
    print(f'Validated {len(skills)} skills, Claude invocation flags, and local links.')
    print(f'SKILL.md files: {total} UTF-8 bytes (not a token count).')
