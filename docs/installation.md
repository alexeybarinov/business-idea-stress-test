# Install Business Idea Stress Test

**[Back to README](../README.md)** · **[Quick start](quickstart.md)** · **[FAQ & troubleshooting](faq.md)**

This is an **instruction-only Agent Skill**: it has no runtime Python packages, API keys, background agents, or paid services. The host's own tools determine how thoroughly it can verify claims. Internet research and file analysis are strongly recommended for full evaluations but are not prerequisites to install the skill.

**Choose one method for each host.** Do not install the same skill both with a host's plugin marketplace and `npx skills` at once: duplicate skill names can cause ambiguous activation. Review external skills before enabling them.

> **Status of these instructions:** Installation locations and commands are based on the linked host documentation (checked September 2026). The skill bundle is structurally validated in CI. We cannot guarantee that every third-party host or account tier loads it correctly; use the verification step after installing. Installation in one product does **not** automatically install it in another.

## At a glance

| Product | Recommended route | Verification / invocation |
|---|---|---|
| **ChatGPT with Skills access** | [Upload the official release ZIP](#chatgpt-web--skills-enabled-accounts) | Mention `@Business Idea Stress Test` if available, or explicitly ask to use the skill |
| **Codex CLI / IDE** | `npx skills add alexeybarinov/business-idea-stress-test -g -a codex` | List skills or mention `$business-idea-stress-test` |
| **Claude Code** | `npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code` | Ask Claude to list its skills; invoke `/business-idea-stress-test` |
| **Claude.ai (web)** | [Upload the release ZIP](#claudeai-web) | Enable the skill and ask for a business idea stress test |
| **Gemini CLI** | `gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git` | `gemini skills list`, then start the interview |
| **Cursor** | `npx skills add alexeybarinov/business-idea-stress-test -g -a cursor` | Inspect detected skills, explicitly request the skill |
| **GitHub Copilot CLI** | `npx skills add alexeybarinov/business-idea-stress-test -g -a github-copilot` | `/skills reload` then `/skills info business-idea-stress-test` |
| **OpenCode** | `npx skills add alexeybarinov/business-idea-stress-test -g -a opencode` | Inspect installed skills; explicitly request the skill |
| **Other Agent Skills hosts** | [Universal CLI](#universal-agent-skills-cli) or [manual installation](#manual-installation) | Check the host's own activation mechanism |

`-g` means **user/global scope**, available across projects. Omit it to install only in your current working project, in which case run the command *inside that project*. The `npx` method requires Node.js and a working npm/npx installation; no Node.js is needed to use the skill after manual installation. The **first run may ask permission** to install/use the `skills` CLI.

## ChatGPT web / Skills-enabled accounts

1. Open [Releases](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) and download the asset named `business-idea-stress-test-vX.Y.Z.zip` (the *skill-only ZIP*, not GitHub's auto-generated **Source code ZIP**)
2. Open ChatGPT → **Plugins → Skills**, then choose the option to create/upload a skill if offered for your account
3. Select **Upload from your computer**, choose the release ZIP and complete the host's review/scan
4. Start a separate conversation for each idea and enter: `Use Business Idea Stress Test. Interview me about my business idea, one high-impact question at a time.`

Some ChatGPT plans, products and workspaces do not offer custom Skills upload. An ordinary chat with the copied instructions is a possible *manual alternative*, not an installed Skill. **The public GitHub repository is not itself a published ChatGPT Plugin Directory listing.** The `agents/openai.yaml` file supplies optional name, prompt and icon metadata for OpenAI hosts that support it.

**Update:** download the newer release ZIP and follow your workspace's replace/upload process; do not assume that uploads track GitHub automatically.

Official guidance: [OpenAI Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) and [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Codex CLI / IDE

Install globally with the open Agent Skills CLI:

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

Or install the current release for just one project by omitting `-g` and running inside that project's root directory. Open Codex, inspect available skills, and invoke:

```text
$business-idea-stress-test I have an idea for a business. Interview me before researching it.
```

If your session does not detect the new skill, restart Codex. Current Codex guidance discovers user skills in `~/.agents/skills/` and repo skills in `.agents/skills/`.

**Update:** `npx skills update business-idea-stress-test -g`; manually installed files must be replaced manually. **Remove:** `npx skills remove business-idea-stress-test -g`.

Official guidance: [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills).

## Claude Code

Install globally:

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

Or install only for one project by omitting `-g`. Native Claude Code skill directories are `~/.claude/skills/<skill-name>/` (personal) and `.claude/skills/<skill-name>/` (project).

In Claude Code, invoke:

```text
/business-idea-stress-test Challenge my new business idea. Begin with founder questions.
```

**Important:** This project is **not** listed as a Claude Code Marketplace plugin. Do not run `/plugin install business-idea-stress-test` unless a verified plugin marketplace listing is published in the future. For this repository, use `npx skills` or a manual skill folder.

**Update:** `npx skills update business-idea-stress-test -g`. If a newly created skills directory does not appear, restart Claude Code.

Official guidance: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Claude.ai web

1. Download the **skill-only** ZIP from [Releases](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
2. In claude.ai, go to **Customize → Skills**; select **+ → Create skill → Upload a skill**
3. Select the ZIP and enable the resulting skill
4. Start a new conversation and ask: `Use Business Idea Stress Test. Interview me about this business concept...`

Your plan/account must support custom skills. Claude's UI and feature availability can change. Updating a manual upload requires uploading an updated ZIP.

Official guidance: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Gemini CLI

Gemini CLI includes its own installer:

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
# Inspect the installed skills:
gemini skills list
```

Alternatively, use the cross-host Agent Skills CLI:

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a gemini-cli
```

For scope selection and troubleshooting, consult `gemini skills install --help`. In an interactive session, use `/skills list` or reload/discover skills with the current Gemini commands. Ask Gemini to use `business-idea-stress-test` to interview you. If the native installer does not discover a skill at the repository root with your CLI version, try the universal installer or manual installation.

Official guidance: [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/).

## Cursor, GitHub Copilot and OpenCode

```bash
# Install to just one selected host (global user scope):
npx skills add alexeybarinov/business-idea-stress-test -g -a cursor
npx skills add alexeybarinov/business-idea-stress-test -g -a github-copilot
npx skills add alexeybarinov/business-idea-stress-test -g -a opencode
```

These are **alternative commands**, not three mandatory commands. Use the host you actually run. Copilot CLI also supports manually installed personal skills at `~/.copilot/skills/` and repository skills in `.github/skills/`, `.claude/skills/` or `.agents/skills/`. After a manual Copilot CLI installation, run `/skills reload` and `/skills info business-idea-stress-test`.

Official guidance: [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Agent Skills CLI](https://github.com/vercel-labs/skills).

## Universal Agent Skills CLI

```bash
# List skills detected in this repository without installing:
npx skills add alexeybarinov/business-idea-stress-test --list

# Install interactively, choose one or more agents:
npx skills add alexeybarinov/business-idea-stress-test

# Update a global installation:
npx skills update business-idea-stress-test -g

# Inspect or remove a global installation:
npx skills list -g
npx skills remove business-idea-stress-test -g
```

This distribution uses a root-level `SKILL.md`, supported by the open Agent Skills format. Client support varies. The repository **does not** ship a proprietary installer for each AI product.

Official guidance: [Vercel Labs skills CLI](https://github.com/vercel-labs/skills), [Agent Skills specification](https://agentskills.io/specification).

## Manual installation

1. Download the **skill-only** release ZIP and unzip it
2. Keep the entire `business-idea-stress-test/` folder intact, especially `SKILL.md`, `references/` and `agents/openai.yaml` when supported
3. Copy the folder into the appropriate *skills parent directory* listed below, then refresh/restart the host if necessary

```text
Codex:           ~/.agents/skills/business-idea-stress-test/
Claude Code:     ~/.claude/skills/business-idea-stress-test/
Gemini CLI:      ~/.gemini/skills/business-idea-stress-test/
Cursor:          ~/.cursor/skills/business-idea-stress-test/
GitHub Copilot:  ~/.copilot/skills/business-idea-stress-test/
```

Use the actual home-directory path on Windows rather than typing `~` if your shell does not expand it. For project-only installation, see the host documentation linked above. A skills directory must contain the skill folder, not only the bare `SKILL.md` file, so relative references remain available.

## Verify by trying a realistic prompt

```text
Use business-idea-stress-test. I'm considering a subscription service for
[buyer segment] in [country]. I know my budget but do not know the market size.
Ask one important question at a time. Do not guess unknown financial inputs.
```

A correctly loaded skill should begin by clarifying *what the business is, who pays, and where it operates*, instead of immediately inventing a market report. Some agents auto-activate relevant skills, but **explicit invocation** avoids uncertainty.

If installation or invocation fails, see [FAQ & troubleshooting](faq.md). For future versions, monitor [Releases](https://github.com/alexeybarinov/business-idea-stress-test/releases); auto-update behavior depends on the installation method.
