# FAQ & troubleshooting

**[Back to README](../README.md)** · **[Installation](installation.md)** · **[Quick start](quickstart.md)**

## What is this: a skill, an autonomous agent team, or a business consultant?

An instruction-only **Agent Skill**. It stages a one-time founder interview and structured analytical workflow using capabilities your host already provides. It does **not** hire human advisors, schedule recurring meetings, run seven separate models or guarantee a business verdict.

## Does it need an API key, Python, paid data or Node.js?

Not for normal skill use. `npx skills` uses Node.js only *during installation* if you choose that route. Python and PyYAML are only required to run maintainer validation/packaging scripts; those scripts are **not bundled into the installed ZIP**. Web access, document analysis and your own source material are recommended for an evidence-backed report. Premium databases are **not included**.

## Will it access the internet and verify current competitor prices?

Only if your host provides browsing/research tools and permits their use. If it cannot verify a source, it should flag the gap and offer a manual validation plan. Current pricing cannot be guaranteed, even when published by a competitor; record the observation date.

## How much time does a complete analysis take?

No fixed duration. The number of founder answers, research scope, region, data availability and host limits determine it. This skill cannot perform unattended background work unless the host separately provides and authorizes that feature.

## Does every supported host behave identically?

No. The underlying **Agent Skills** format is portable, but activation, tool access, discovery and upload entitlement differ. Cross-host commands in the installation guide come from the corresponding official documentation; actual end-to-end testing is **not claimed for every host**.

## Why doesn't my skill appear in ChatGPT?

Custom Skills upload depends on your plan, workspace permissions and product surface. Check **Plugins → Skills**, then consult [OpenAI's current Skills guidance](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). The public GitHub page is **not** a Plugin Directory listing and does not install itself into your account.

## Claude Code can't see the skill

Check `~/.claude/skills/business-idea-stress-test/SKILL.md` (or the repository-level equivalent). Make sure the `references/` directory is beside `SKILL.md`. Avoid installing this skill twice under different names or installation systems. Restart Claude Code if it didn't previously watch the skills parent directory.

## Codex or Cursor can't find it

Run `npx skills list -g` and check the selected agent/scope. A project-scoped installation is only discoverable in the project in which it was installed. In Codex, try `$business-idea-stress-test` after reloading/restarting if necessary; in other hosts, explicitly name the skill in your prompt.

## Claude.ai says the ZIP structure is wrong

Download the **release asset** ZIP rather than GitHub's auto-generated source archive. The release package contains a top-level `business-idea-stress-test/` folder with a `SKILL.md` and its references; do not flatten its contents.

## Is it safe to share sensitive startup data?

Read your AI host's privacy and retention settings first. You can give estimates, ranges or anonymized information. Do not put credentials, customer contact lists, internal secrets, financial account numbers, or confidential third-party material into a public GitHub issue. The skill itself has no external data collection endpoint; what a model or its browsing tools do is controlled by the host.

## Are the seven credited skills installed as dependencies?

No. The seven linked projects **inspired** this newly written workflow; their files and commercial tools are **not bundled or automatically executed**. Their ownership and licenses are independent. See [source acknowledgments](../references/sources.md).

## How do I update or roll back?

If installed via `npx skills`, use `npx skills update business-idea-stress-test -g` for global installations. For ChatGPT or Claude.ai manual uploads, download and re-upload the intended release. To roll back, select the earlier version under [Releases](https://github.com/alexeybarinov/business-idea-stress-test/releases) and follow your host's manual replacement process. **Updating via the CLI may track the latest repository commit** rather than a specific older release; use a release ZIP when you need a pinned version.

## Where do I report a mistake or suggest a translation improvement?

Use [GitHub Issues](https://github.com/alexeybarinov/business-idea-stress-test/issues), and include a reproducible, non-sensitive example. Check [CONTRIBUTING](../CONTRIBUTING.md) for maintainer instructions.
