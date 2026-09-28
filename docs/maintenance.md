# Maintainer verification and maintenance

[← Back to README](../README.md) · [Installation](installation.md) · [Contributor guide](../CONTRIBUTING.md)

This checklist separates checks we can automate from those that require a particular product, account, operating system or network

## Local, repeatable checks

```bash
python -m pip install pyyaml
python scripts/validate_skill.py
python scripts/package_skill.py
```

`validate_skill.py` verifies skill YAML metadata, matching SemVer, core files, relative Markdown links, all eight-language navigation pages, optional OpenAI metadata, the icon file and GitHub social preview dimensions/size. `package_skill.py` produces a skill-only ZIP and verifies its contents and integrity

**These checks do NOT prove:** that a client installed or activated the skill successfully, that web research data is accurate, that all external URLs are currently online or that every supported subscription has the same feature set

## Manual host smoke test

1. Install using the steps for the actual host in [installation.md](installation.md)
2. Start a fresh conversation: `Use Business Idea Stress Test. I want to evaluate an on-demand mobile bicycle repair idea. Start by asking me one high-impact founder question at a time.`
3. Confirm the model **does not immediately produce a confident go/no-go answer** and asks one relevant, non-redundant question
4. Supply incomplete answers and verify that missing financial inputs remain **U** (unknown) or **H** (hypothesis), not invented facts
5. Request market research. Verify that sources are dated and region-specific **if** the host actually has web tools, or that unavailable browsing is explicitly disclosed
6. Request the red-team stage. Check that the model does not claim a panel of independent experts if it is merely adopting multiple analytical perspectives
7. Record tested host, app/CLI version, operating system, result, date and any caveats in a maintainer issue or review

**Cross-host support status:** Installation directions have been researched, and repository CI validates packaging. A broad end-to-end compatibility claim should not be made until the actual host matrix is executed

## Release protocol

- Update `CHANGELOG.md`, `VERSION` and `SKILL.md` frontmatter together
- Run both local checks, then push via reviewed pull request when practical
- Wait for both repository validation and release workflows to succeed
- Verify new `vX.Y.Z` tag and its attached ZIP in GitHub Releases
- Validate the downloaded release archive before announcing it
- Do not retroactively move published version tags or silently overwrite released assets
