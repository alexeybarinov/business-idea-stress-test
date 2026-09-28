#!/usr/bin/env python3
"""Build the portable skill ZIP, excluding maintainer scripts, README and translations."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / 'scripts/validate_skill.py')], check=True)
version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
out = ROOT / 'dist' / f'business-idea-stress-test-v{version}.zip'
out.parent.mkdir(exist_ok=True)
paths = [
    ROOT / 'SKILL.md', ROOT / 'agents' / 'openai.yaml',
    *(ROOT / 'references').glob('*.md'),
    ROOT / 'assets' / 'icon.png', ROOT / 'assets' / 'icon-small.svg',
]
with ZipFile(out, 'w', ZIP_DEFLATED, compresslevel=9) as archive:
    for item in sorted(paths):
        archive.write(item, arcname=str(Path('business-idea-stress-test') / item.relative_to(ROOT)))
with ZipFile(out) as archive:
    filenames = set(archive.namelist())
    required = {
        'business-idea-stress-test/SKILL.md',
        'business-idea-stress-test/agents/openai.yaml',
        'business-idea-stress-test/assets/icon-small.svg',
        'business-idea-stress-test/assets/icon.png',
    }
    assert required.issubset(filenames), 'Missing required runtime files'
    assert archive.testzip() is None, 'Corrupt skill ZIP'
    assert all(n.startswith('business-idea-stress-test/') for n in filenames), 'Invalid ZIP root'
    assert len(filenames) <= 200, 'Too many files for common skill upload hosts'
print(f'PASS: {out.relative_to(ROOT)} ({out.stat().st_size} bytes, {len(filenames)} runtime files)')
