#!/usr/bin/env python3
"""Build a compact ZIP containing only installable skill resources."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT/'scripts/validate_skill.py')], check=True)
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
out=ROOT/'dist'/f'business-idea-stress-test-v{version}.zip'
out.parent.mkdir(exist_ok=True)
paths=[ROOT/'SKILL.md', *(ROOT/'references').glob('*.md'), ROOT/'assets'/'icon.png']
with ZipFile(out,'w',ZIP_DEFLATED,compresslevel=9) as archive:
    for item in sorted(paths):
        archive.write(item,arcname=str(Path('business-idea-stress-test')/item.relative_to(ROOT)))
with ZipFile(out) as archive:
    filenames=set(archive.namelist())
    assert 'business-idea-stress-test/SKILL.md' in filenames
    assert all(archive.testzip() is None for _ in range(1))
print(f'PASS: {out.relative_to(ROOT)} ({out.stat().st_size} bytes, {len(filenames)} files)')
