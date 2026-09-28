#!/usr/bin/env python3
"""Check skill schema, version metadata, localized documentation and install packaging."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def expect(condition, message):
    if not condition:
        ERRORS.append(message)


def yaml_file(path):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        expect(isinstance(data, dict), f"{path}: YAML must be a mapping")
        return data if isinstance(data, dict) else {}
    except (OSError, yaml.YAMLError) as exc:
        ERRORS.append(f"{path}: invalid YAML ({exc})")
        return {}


skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
expect(len(parts) == 3 and parts[0].strip() == "", "SKILL.md must start with YAML frontmatter")
meta = yaml.safe_load(parts[1]) if len(parts) == 3 else {}
expect(isinstance(meta, dict), "SKILL.md frontmatter must be a mapping")
meta = meta if isinstance(meta, dict) else {}
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
expect(re.fullmatch(r"\d+\.\d+\.\d+", version) is not None, "VERSION must use X.Y.Z")
expect(meta.get("name") == "business-idea-stress-test", "Unexpected skill name")
expect(isinstance(meta.get("description"), str) and 1 <= len(meta.get("description", "")) <= 1024, "Invalid skill description")
expect(meta.get("license") == "MIT", "SKILL.md must declare the project's MIT license")
expect(meta.get("metadata", {}).get("version") == version, "SKILL.md version must match VERSION")
expect(f"[{version}]" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), "CHANGELOG must include current version")

required = [
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md",
    "assets/icon.png", "assets/icon-small.svg", "assets/header.svg", "agents/openai.yaml",
    "docs/installation.md", "docs/quickstart.md", "docs/faq.md",
    "examples/example-session.md", "references/intake.md", "references/validation.md",
    "references/market.md", "references/customer.md", "references/competition.md",
    "references/finance.md", "references/red-team.md", "references/report.md", "references/sources.md",
]
langs = ["ru", "zh-CN", "es", "de", "fr", "pt-BR", "ja"]
required += [f"locales/README.{lang}.md" for lang in langs]
for name in required:
    expect((ROOT / name).is_file(), f"Missing required file: {name}")
for name in re.findall(r"\]\((references/[^)#]+\.md)\)", text):
    expect((ROOT / name).is_file(), f"Broken reference from SKILL.md: {name}")

# Validate optional OpenAI metadata: no dependencies or tools are requested.
ui = yaml_file(ROOT / "agents/openai.yaml")
interface = ui.get("interface", {})
expect(interface.get("display_name") == "Business Idea Stress Test", "Unexpected OpenAI display name")
for field in ("icon_small", "icon_large"):
    value = interface.get(field)
    expect(isinstance(value, str) and (ROOT / value).is_file(), f"Missing OpenAI UI image: {field}")
expect(not ui.get("dependencies"), "The instruction-only bundle should not declare external dependencies")
icon_bytes = (ROOT / "assets/icon.png").read_bytes()
expect(icon_bytes.startswith(b"\x89PNG\r\n\x1a\n"), "Logo file is not a PNG")
expect(len(icon_bytes) < 250000, "Icon should be below 250 KB")

# Validate relative links across the README, all guides and seven localized pages.
# External URLs, mailto links and in-page anchors are intentionally excluded.
docs = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")),
        *sorted((ROOT / "locales").glob("README.*.md"))]
link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
for file in docs:
    body = file.read_text(encoding="utf-8")
    for raw_link in link_re.findall(body):
        link = raw_link.split("#", 1)[0].strip()
        if not link or "://" in link or link.startswith(("mailto:", "#")):
            continue
        target = file.parent / link
        expect(target.exists(), f"Broken local link from {file.relative_to(ROOT)}: {raw_link}")

# Every translation must have the complete language switcher and actionable setup.
links = ["../README.md", *[f"README.{lang}.md" for lang in langs]]
for lang in langs:
    body = (ROOT / f"locales/README.{lang}.md").read_text(encoding="utf-8")
    for link in links:
        expect(f"]({link})" in body, f"{lang}: missing language navigation to {link}")
    expect("business-idea-stress-test" in body, f"{lang}: missing actual install example")
    expect("releases/latest" in body, f"{lang}: missing versioned download link")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
for lang in langs:
    expect(f"locales/README.{lang}.md" in readme, f"Main README: missing language link {lang}")

if ERRORS:
    for message in ERRORS:
        print("ERROR:", message)
    sys.exit(1)
print(f"PASS: schema, v{version}, OpenAI icons, {len(docs)} documentation files and 8-language navigation")
