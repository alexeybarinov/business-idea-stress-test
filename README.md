<div align="center">
  <img src="assets/icon.png" alt="Business Idea Stress Test: business advisors examining a bright idea" width="140" height="140">

  # Business Idea Stress Test

  **Don't fall in love with your business idea. Stress-test it.**

  An open-source, evidence-first **ChatGPT / Agent Skills** workflow that challenges a business concept *before* you invest serious time or money.

  ![Version](https://img.shields.io/badge/version-v1.0.0-2563eb?style=flat-square)
  ![Skill](https://img.shields.io/badge/format-Agent%20Skills-0f766e?style=flat-square)
  ![License](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square)
  ![Dependencies](https://img.shields.io/badge/runtime%20dependencies-none-64748b?style=flat-square)

  [**Install**](#installation) · [**How it works**](#the-six-stage-stress-test) · [**Example prompts**](#example-prompts) · [**Acknowledgments**](#standing-on-the-shoulders-of-the-community) · [**Releases**](#versioning-and-releases)
</div>

![Business Idea Stress Test cover: interview, demand, competitors, finances, adversarial review](assets/header.svg)

> [!IMPORTANT]
> This project is a **critical-thinking workflow, not a business-success predictor**. Every decisive claim should be linked to evidence or labeled as an assumption. One AI model simulating multiple viewpoints is **not** an independent panel of experts.

## What problem does it solve?

A business idea can sound compelling before anyone asks the expensive questions: Does a real buyer have this problem? Who currently solves it? Why switch? What does customer acquisition cost? Can the operation fulfill the promise? What would make the founder walk away?

**Business Idea Stress Test** turns those questions into a one-off process instead of producing a glossy business plan with optimistic numbers. It interviews the founder, researches external evidence when supported by the host, scrutinizes unit economics, and designs a cheap experiment that could actually *disprove* the thesis.

### What you get

| Capability | Outcome |
|---|---|
| Founder interview | Structured idea brief and explicit unanswered questions |
| Early validation | Key hypothesis, real substitutes, potential fatal blockers |
| Market and buyer research | Geographic market boundaries, customer pain and evidence gaps |
| Competitor profiling | Documented alternatives with comparable, dated prices where available |
| Financial and operational review | Worked unit economics, cash exposure, capacity, and conditional scenarios |
| Adversarial critique | Strongest argument against the idea and 12-month failure pre-mortem |
| Decision brief | Conditional evidence assessment and a bounded, measurable test |

## The six-stage stress test

```text
            YOUR IDEA
                │
     1. FOUNDER INTERVIEW
        One question at a time
                │
     2. EARLY VALIDATION
        Hypotheses + fatal blockers
                │
     3. EXTERNAL RESEARCH
        Market · Buyers · Competitors
                │
     4. FINANCIAL REALITY
        Unit economics · Cash · Capacity
                │
     5. ADVERSARIAL REVIEW
        Strongest countercase · Pre-mortem
                │
     6. DECISION & LEAN TEST
        Evidence · Test budget · Stop rules
```

The workflow is **adaptive**. A serious early blocker may change the research order. Missing market or finance data must remain visibly missing rather than being filled with fictional statistics.

## Installation

### Option A — ChatGPT Skills

1. Download the skill-only ZIP from the project's **GitHub Releases** page (after the first release is published). The archive is named `business-idea-stress-test-vX.Y.Z.zip`
2. In ChatGPT, open **Plugins → Skills** and select the option to **create/upload a skill** if your workspace supports it
3. Upload the ZIP, review the permissions/instructions shown, and complete the installation
4. Open a **new chat for each business idea** and type: `Use Business Idea Stress Test. I want to stress-test a business idea. Start by interviewing me.`

ChatGPT availability and menu wording may vary by plan and workspace. Refer to [OpenAI's current Skills guidance](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). No upstream commercial service is required merely to run these instructions

### Option B — Another compatible Agent Skills client

If your client supports the [open Agent Skills format](https://agentskills.io/specification), place the repository's `SKILL.md`, `references/`, and optional `assets/` in one folder named `business-idea-stress-test`, then follow **your client's** skill discovery/install instructions. Automatic activation and the precise install command depend on the host

> [!NOTE]
> The skill does not require locally installing the seven projects that inspired it. Their ideas were adapted into newly written instructions; their code, paid APIs, and original skill files are **not bundled**

## Example prompts

**Start with a blank slate**

```text
Use Business Idea Stress Test. I have a new business idea.
Ask me one important question at a time. Research the market only when
we've resolved the basic assumptions. I want an evidence-based result,
not automatic encouragement.
```

**Start with context**

```text
Stress-test this idea: [description]
Target buyers: [segment / unknown]
Location: [country / city]
Available starting budget: [amount / unknown]
My biggest worry: [risk / unknown]
Begin with the missing high-impact questions.
```

**Continue or challenge harder**

```text
Continue with the next unfinished stage.
Grill harder: challenge the three assumptions most likely to overturn the conclusion.
Show your evidence ledger and identify the weak sources.
Re-evaluate the conclusion using these new customer interview notes: [notes]
```

## Built-in safeguards

- **Evidence ledger:** distinguish **F** (verified fact, labeled by origin), **E** (dated external estimate), **C** (transparent calculation), **H** (untested hypothesis), and **U** (unknown)
- **No invented research:** no fictional buyers, unsupported competitor numbers, fake sources, synthetic interviews masquerading as real customers, or unmeasured CAC presented as observed
- **Finance clarity:** GMV is not automatically intermediary revenue; revenue is not profit; profit is not cash flow; conservative/base/upside cases are *scenarios*, not guaranteed forecasts
- **Geographic and legal boundaries:** match research to the user's actual market; consult current primary material for regulatory questions; flag issues requiring professional advice
- **No phantom agents:** multiple decision-making perspectives inside one model do not constitute independent AI models or real human advisors
- **Consent and realistic tools:** no unsolicited customer contact, spending, subscriptions, or claimed paid-API access without authorization and actual tool support

## Repository layout

```text
business-idea-stress-test/
├── SKILL.md                    # Entrypoint for compatible AI agents
├── references/                 # Loaded as each stage becomes relevant
│   ├── intake.md
│   ├── validation.md
│   ├── market.md
│   ├── customer.md
│   ├── competition.md
│   ├── finance.md
│   ├── red-team.md
│   ├── report.md
│   └── sources.md               # Full upstream credits + scope limitations
├── assets/
│   ├── icon.png                 # Visual mark, generated for this project
│   └── header.svg               # GitHub README artwork
├── examples/
│   └── example-session.md
├── scripts/
│   ├── validate_skill.py        # Maintainer-only quality checks
│   └── package_skill.py         # Creates a skill-only installation ZIP
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/             # CI and versioned GitHub release
├── VERSION                     # Current SemVer version
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

## Standing on the shoulders of the community

**Thank you** to the people who openly published the tools and ideas that inspired this independently written workflow:

| Inspiration | Author/project | What influenced this skill |
|---|---|---|
| [Grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | **Matt Pocock** | Sequential, decision-tree questioning |
| [Idea Validator](https://github.com/BuildGreatProducts/builder-os/blob/main/skills/idea-validator/SKILL.md) | **BuildGreatProducts** | Early hypothesis validation and critical blockers |
| [Market Researcher](https://github.com/xcrrr/claude-skills/blob/main/skills/business/market-researcher/SKILL.md) | **xcrrr** | Market scope, segmentation, and sizing discipline |
| [Customer Research](https://github.com/coreyhaines31/marketingskills/blob/main/skills/customer-research/SKILL.md) | **Corey Haines** | Buyer insights grounded in actual evidence |
| [Competitor Profiling](https://github.com/coreyhaines31/marketingskills/blob/main/skills/competitor-profiling/SKILL.md) | **Corey Haines** | Structured analysis of competitive alternatives |
| [Startup Analyst](https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/startup-analyst/SKILL.md) | **sickn33** / Agentic Awesome Skills | Startup finance and operational realities |
| [Devil's Advocate](https://github.com/jukeyman/jukeyman-skills/blob/main/skills/productivity--pm-ai-partner--devil-advocate/SKILL.md) | **jukeyman** | Constructive, rigorous counterarguments |

We appreciate the original maintainers' work. **This project is unaffiliated with and not endorsed by those authors.** We do not redistribute their original skill files or copy their scripts. See [references/sources.md](references/sources.md) for attribution details and limitations

## Versioning and releases

This project follows [Semantic Versioning](https://semver.org/):

- **Patch:** `v1.0.1` — clarifications and fixes that preserve the intended workflow
- **Minor:** `v1.1.0` — new optional capabilities or backward-compatible workflow extensions
- **Major:** `v2.0.0` — meaningful breaking changes to usage, outputs, or skill structure

`VERSION` and `SKILL.md` metadata must match. Changes are documented in [CHANGELOG.md](CHANGELOG.md). The CI validates files on each push/PR, and the GitHub Actions release workflow can create a versioned tag, GitHub Release, and skill-only ZIP **when a new VERSION is pushed to the default branch** (subject to the repository's Actions permissions and settings)

## Contributing and security

- Found an error, missing risk category, outdated assumption, or broken source? Open an issue using the included templates
- See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and run the maintainer checks
- Read [SECURITY.md](SECURITY.md) before reporting sensitive security problems

**License:** [MIT](LICENSE), applying to the original files in this repository. Each linked upstream project retains its own license
