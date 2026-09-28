# Stage 4 — Financial and operational reality check

**Methodological inspiration:** sickn33's Startup Analyst. Do not assume the business will be profitable. Tailor the model to the actual unit of sale: a one-off product, local service, subscription/SaaS, intermediary, aggregator, or long-cycle B2B arrangement. For taxes, labor, licensing, wages, and other changing local facts, use current jurisdiction-specific sources or mark the inputs as **unverified**.

## Required inputs

- Modeling currency, tax/legal jurisdiction, modeling period, unit of sale, and role as principal or agent where relevant
- Price or average transaction size, sales seasonality, repeat purchase frequency, and payment settlement timing
- **Variable expenses:** cost of fulfillment, logistics, payment/platform fees, discounts, refunds, contractor labor, support, and expected write-offs where supported
- **Fixed expenses:** wages or founder time cost, rent, systems/hosting, insurance, administration, sales channel access, and fixed marketing costs
- **Setup and working capital:** permits, contracts, testing, equipment, hiring/training, supplier deposits, and minimum cash buffer
- **Capacity:** orders actually deliverable, bottlenecks, supplier concentration, and quality constraints
- **Acquisition:** test lead costs, realistic funnel, verified conversion data vs unmeasured assumptions

## Show formulas, substitutions, units, and time periods

### Products and services

```text
Revenue                   = paid orders × actual average order value
Contribution per order    = actual order value − all variable expenses per order
Period contribution       = paid orders × contribution per order
Operating result pre-tax  = period contribution − fixed costs over the same period
Break-even paid orders    = ceil(period fixed costs / positive contribution per order)
```

Only calculate order break-even if the per-order contribution is **positive** and all material modeled costs are in comparable units. Explain otherwise.

### Marketplaces, agents, and aggregators

```text
Intermediary model revenue = GMV × applicable earned take rate + other recognized earned fees
Contribution per order    = earned commission and fees − payment fees − refunds/compensation
                            − other per-order variable costs
```

**GMV is not automatically revenue** for an intermediary. Principal/agent accounting and applicable local standards govern recognition; do not issue an accounting ruling without sufficient facts.

### SaaS and subscriptions

```text
MRR                         = active paying accounts × actual monthly realized payment
Monthly account contribution = monthly realized payment − variable servicing costs
Observed CAC                = actual acquisition spending / actual new customers acquired
```

Calculate **observed CAC** only when numerator and denominator are measured over a compatible cohort and period. Before measurement, present explicit hypothetical acquisition scenarios. Calculate **LTV** only when retention/churn and economics are defensible. Never silently assume infinite lifetime or zero churn.

### Cash flow is different from accounting profit

Account for supplier prepayments, settlement delays, deposits, refunds, short-term financing, and working capital. Negative contribution per order is usually exacerbated by increasing volume, before any separately evidenced offsetting effects.

## Scenarios and sensitivity

Produce **conservative, base, and upside conditional scenarios**, not forecasts of what will happen. For each, state: buyers/orders, frequency, price, variable costs, measured vs assumed funnel conversion, operational capacity, fixed costs, monthly operating result, initial cash required, and available runway. Label every material input F/E/C/H/U using the evidence ledger definitions in `SKILL.md`.

If the founder does not know the price or acquisition cost, build a **sensitivity grid** and solve for the threshold necessary to break even. Do not report exact-looking numbers when input uncertainty is very large. Ensure scenario demand does not exceed plausible delivery capacity.

## Overlooked costs to check

Refunds and cancellations, payment processor fees, foreign exchange, VAT/sales taxes, permits and licenses, defects, founder time, contractor idle time, failed marketing tests, single-channel reliance, B2B receivables, and cash shortfalls during growth.

### Deliverables

Source-linked input table; worked formulas with units; three clearly conditional scenarios *or* a reason it is premature to build them; break-even conditions; sensitivity to fragile assumptions; and the **three measurements** that should be collected first.
