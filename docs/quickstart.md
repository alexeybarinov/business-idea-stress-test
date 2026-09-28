# Quick start: stress-test your first business idea

**[Back to README](../README.md)** · **[Installation guide](installation.md)** · **[FAQ](faq.md)**

You do not need a business plan, financial model or a list of competitors before starting. The skill is designed to find missing information, not pretend you know it.

## 1. Open a new conversation for one idea

After installing the skill, invoke it explicitly if your host supports it. In ChatGPT with Skills access, mention it by name or use the `@` picker when offered. In Codex, try `$business-idea-stress-test`. In Claude Code, try `/business-idea-stress-test`.

Paste this into your first message (replace only what you already know):

```text
Use Business Idea Stress Test. I have this business idea:
[Describe what you want to sell, who you think would pay, and where.]

My available budget: [amount or "unknown"]
My biggest concern: [concern or "unknown"]

Start with the founder interview. Ask one high-impact question at a time.
I want evidence that might disprove the idea, not motivational feedback.
```

## 2. Answer the questions candidly

The interview separates founder-provided information from external evidence. `I don't know` is a valid answer. If something is confidential, give a broad range or ask the assistant to continue without it. Never disclose credentials, private customer data or unnecessary personal information.

A business idea might have fatal regulatory or fulfillment blockers. If a critical issue emerges, the skill should investigate it **before** producing pages of speculative market analysis.

## 3. Supply existing information if you have it

Optional: competitor URLs, industry reports, existing customer interview notes, supplier quotes, landing-page results or cost estimates. Tell the assistant the region and observation date. It must not treat an old price or different country's market data as current local evidence.

## 4. Review the evidence and the unit economics

Ask:

```text
Show me the five claims that matter most to the result. For each, show
its source, date, geography and whether it is verified, estimated,
calculated, hypothetical or unknown. Identify my weakest assumption.
```

Financial scenarios must show all material inputs and distinguish your own revenue from marketplace transaction volume, profit from cash flow, and measured acquisition cost from a guess.

## 5. Demand the opposing case and a cheap experiment

```text
Run the toughest defensible counterargument against this idea.
What observable outcome would change your conclusion?
Design the cheapest ethical test I can run before committing more money.
```

The final deliverable is a **conditional decision brief**, not a guarantee that a business will succeed or fail. Human customer interviews, actual purchases and professional legal review are sometimes required before committing capital.

## 6. Continue later without redoing the interview

If the host supports conversation history, continue in the same chat. If it does not, ask it to produce a **handoff card** with founder inputs, sources, completed stages and unanswered questions. Open a new chat, explicitly invoke the skill, and paste that card with: `Continue from this verified checkpoint; do not invent missing stages.`

For an entirely separate idea, start a **new chat**, and preferably isolate project/workspace context when your host supports it.

See [a fictional example session](../examples/example-session.md), an [illustrative final report](../examples/sample-output.md), or the [installation guide](installation.md)
