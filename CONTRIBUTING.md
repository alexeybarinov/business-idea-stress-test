# Contributing

Thank you for helping make business idea evaluation more evidence-driven and less promotional.

## Before proposing changes

1. Check existing issues for related suggestions or identified errors
2. Describe the actual analysis failure your change addresses and supply a minimal example when possible
3. Keep advice jurisdiction-aware, evidence-led, and realistic for users without paid data products
4. Do not copy third-party skill code or documentation without license review, explicit attribution, and a clear reason

## Local checks

You only need Python 3.10+ and PyYAML **for maintainer validation**, not for normal use of the skill:

```bash
python -m pip install pyyaml
python scripts/validate_skill.py
python scripts/package_skill.py
```

The packaging script produces `dist/business-idea-stress-test-vX.Y.Z.zip` with only the installation content. Neither helper runs inside the skill itself

## Change rules

- Keep the required `SKILL.md` YAML frontmatter valid according to the [Agent Skills specification](https://agentskills.io/specification)
- Write instructions and documentation in clear, accessible **English**. The skill may still answer users in their preferred language
- Preserve relative references from `SKILL.md`; small focused `references/*.md` files should be loaded only when needed
- Mark facts, external estimates, calculations, hypotheses, and unknowns separately; no invented citations or fabricated user studies
- Record user-visible changes in `CHANGELOG.md`
- If semantics change, update `VERSION`, matching `SKILL.md` metadata. Use major/minor/patch based on the impact
- Include a suggested prompt and a before/after expected behavior when changing the analytical workflow

## Release process

After a pull request is reviewed and merged, update `VERSION`, `SKILL.md` metadata, and `CHANGELOG.md` together for the intended release. Pushing a **new version in VERSION** to the default branch triggers the release workflow, which validates files and attempts to publish `vX.Y.Z` with a skill-only ZIP. A repository maintainer can also invoke the workflow manually if Actions are enabled. Never move an existing version tag to change shipped content: publish a new patch release

## Pull request checklist

- [ ] A concrete user-facing failure or improvement is explained
- [ ] No unlicensed upstream material was copied
- [ ] Documentation and new instructions are English-language
- [ ] New factual claims cite trustworthy sources or are labeled as hypotheses
- [ ] Both local validation and packaging succeed
- [ ] CHANGELOG and version metadata are synchronized if releasing
