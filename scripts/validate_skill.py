#!/usr/bin/env python3
"""Validate the distributable skill and release metadata. Maintainer-only."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []

def expect(condition, message):
    if not condition:
        ERRORS.append(message)

skill = ROOT / 'SKILL.md'
text = skill.read_text(encoding='utf-8')
parts = re.split(r'^---\s*$', text, maxsplit=2, flags=re.MULTILINE)
expect(len(parts) == 3 and parts[0].strip() == '', 'SKILL.md must start with YAML frontmatter')
meta = yaml.safe_load(parts[1]) if len(parts) == 3 else {}
expect(isinstance(meta, dict), 'YAML must contain a mapping')
if isinstance(meta, dict):
    expect(meta.get('name') == 'business-idea-stress-test', 'Unexpected skill name')
    expect(bool(meta.get('description')), 'Missing skill description')
    expect(meta.get('license') == 'MIT', 'License metadata must match LICENSE')
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    expect(bool(re.fullmatch(r'\d+\.\d+\.\d+', version)), 'VERSION must be semantic X.Y.Z')
    expect(meta.get('metadata', {}).get('version') == version, 'SKILL.md version must match VERSION')
    expect(f'[{version}]' in (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8'), 'CHANGELOG must include version')
for path in ('README.md','LICENSE','CHANGELOG.md','CONTRIBUTING.md','SECURITY.md','assets/icon.png','assets/header.svg','references/intake.md','references/validation.md','references/market.md','references/customer.md','references/competition.md','references/finance.md','references/red-team.md','references/report.md','references/sources.md'):
    expect((ROOT/path).is_file(), f'Missing required file: {path}')
for name in re.findall(r'\]\((references/[^)#]+\.md)\)', text):
    expect((ROOT / name).is_file(), f'Broken reference from SKILL.md: {name}')
for name in re.findall(r'\]\((assets/[^)#]+)\)', (ROOT/'README.md').read_text(encoding='utf-8')):
    expect((ROOT / name).is_file(), f'Broken README image: {name}')
raw = (ROOT/'assets/icon.png').read_bytes()
expect(raw[:8] == b'\x89PNG\r\n\x1a\n', 'Icon must be a PNG')
expect(len(raw) < 250000, 'Icon should be below 250KB')
expect(len(meta.get('description','')) <= 1024, 'Description exceeds 1024 characters')
if ERRORS:
    for message in ERRORS: print('ERROR:', message)
    sys.exit(1)
print('PASS: SKILL.md schema, semantic version, assets, stage references and changelog')
