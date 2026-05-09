# Hormozi $100M Frameworks Skill

> A portable, installable skill that lets any AI agent apply Alex Hormozi's complete $100M business framework library. Extracted from all 13 books in the series.

[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/genshin-hermes/hormozi-100m-skill/releases)
[![Books](https://img.shields.io/badge/books-13-green)]()
[![Frameworks](https://img.shields.io/badge/frameworks-47-orange)]()

---

## What This Is

This is a **Hermes Agent skill** — a structured knowledge package that teaches an AI agent how to think, advise, and execute using Alex Hormozi's complete business framework library.

It is **not** a summary. It is an **operational toolkit**:
- **12 core frameworks** with step-by-step application
- **4 ready-to-use templates** (markdown)
- **1 CLI tool** for programmatic framework application
- **47 extracted frameworks** indexed from 13 books
- **~1.2M characters** of source material distilled into actionable playbooks

---

## The 13 Books Covered

| # | Book | Core Framework | Application |
|---|------|---------------|-------------|
| 1 | **$100M Offers** | The Grand Slam Offer, Value Equation, Offer Stacking | Offer creation |
| 2 | **$100M Leads** | Content-Market Fit, The Content Matrix | Lead generation |
| 3 | **$100M Money Models** | Money Model Design, Three Continuity Offers | Revenue architecture |
| 4 | **$100M Lost Chapters** | Advanced Offer Stacking, CAC vs LTGP, Value Grid | Advanced strategies |
| 5 | **$100M Scaling Roadmap** | 10-Stage Scaling (Improvise → Capitalize) | Business scaling |
| 6 | **$100M Branding Playbook** | The Bouquet Metaphor, Audience Selection | Brand building |
| 7 | **$100M Fast Cash Playbook** | Fast Cash Sequence, Prepaid Offers | Cash extraction |
| 8 | **$100M Goated Ads Playbook** | Hook-Meat-CTA, Ad Scaling | Advertising |
| 9 | **$100M Hooks Playbook** | Hook Formula, Verbal/Nonverbal Hooks, Shout Method | Copywriting |
| 10 | **$100M Lead Nurture Playbook** | Follow-Up Grid, Speed to Lead | Sales follow-up |
| 11 | **$100M Lifetime Value Playbook** | LTV Maximization, The Crazy Eight | Customer value |
| 12 | **$100M Pricing Playbook** | Price Raise Justification, Value Communication | Pricing strategy |
| 13 | **$100M Marketing Machine** | Full Funnel Automation, Churn Reduction | Marketing automation |

---

## Core Philosophy

> "The goal is to make an offer so good people feel stupid saying no."

Hormozi's approach rests on four pillars:

1. **Make Offers So Good They Sell Themselves** — The Grand Slam Offer
2. **Get Leads So Cheap It Feels Like Cheating** — Content-Market Fit
3. **Build Money Models That Print Cash** — Revenue Architecture
4. **Scale Without Breaking** — The 10-Stage Roadmap

### The Value Equation

The foundational formula for every offer:

```
Value = (Dream Outcome × Perceived Likelihood of Achievement) / (Time Delay × Effort & Sacrifice)
```

**How to apply:**
- Increase the dream outcome (what they really want)
- Increase perceived likelihood (proof, guarantees, testimonials)
- Decrease time delay (speed to result)
- Decrease effort & sacrifice (make it easy)

---

## What's Inside

### `SKILL.md` — The Master Document (~900 lines)
The core knowledge base. Contains:
- All 12 frameworks with full detail
- Lost Chapters frameworks (CFA, Value Grid, 4 Steps, Offer Types)
- Stage-by-stage scaling roadmap
- The Crazy Eight LTV methods
- Speed to Lead system
- Price raise rules and math
- Retention's 5 Horsemen
- And more

### `scripts/apply-framework.py` — CLI Tool
Apply any framework programmatically:

```bash
python3 scripts/apply-framework.py offer "I run a fitness coaching business"
python3 scripts/apply-framework.py scaling "We're at $50K/month, stuck"
python3 scripts/apply-framework.py pricing "Need to raise prices 20%"
```

**Supported frameworks:** `offer`, `money-model`, `hook`, `ad`, `scaling`, `pricing`, `retention`, `branding`, `lifetime-value`, `lead-nurture`, `fast-cash`

### `templates/` — Ready-to-Use Templates

| Template | Use Case |
|----------|----------|
| `grand-slam-offer.md` | Build an irresistible offer from scratch |
| `hook-swipe-file.md` | Generate 50 hooks in one session |
| `money-model-designer.md` | Design your revenue architecture |
| `scaling-roadmap-checklist.md` | Assess your current stage and next steps |

### `references/` — Index & Audit

| File | Purpose |
|------|---------|
| `framework-index.json` | Machine-readable index of all 13 books, 47 frameworks |
| `audit-protocol.md` | How this skill was built and verified |

---

## Installation

### Option 1: Clone (Recommended)

```bash
git clone https://github.com/genshin-hermes/hormozi-100m-skill.git ~/.hermes/skills/hormozi-100m-frameworks
```

### Option 2: Download Release

Download `hormozi-100m-frameworks.zip` from the [latest release](https://github.com/genshin-hermes/hormozi-100m-skill/releases) and extract to `~/.hermes/skills/`.

### Option 3: Manual Copy

Copy the skill folder to your Hermes skills directory:
```bash
cp -r hormozi-100m-frameworks ~/.hermes/skills/
```

---


### Option 4: Install via skills.sh (Vercel)

You can also install this skill using Vercel's skills.sh ecosystem:

```bash
npx skills install hormozi-100m-skill
```

This makes the skill available to any AI agent that supports the skills.sh format.

## Quick Start

### As a Human User

1. **Read `SKILL.md`** for the framework you need
2. **Use a template** from `templates/` as your starting point
3. **Run the CLI** to get a structured output:
   ```bash
   python3 scripts/apply-framework.py offer "My SaaS helps dentists get more patients"
   ```

### As an AI Agent

Load this skill and reference it when the user asks about:
- Creating offers, pricing, or guarantees
- Lead generation, ads, or hooks
- Scaling a business or building teams
- Revenue models, upsells, or continuity
- Cash extraction or fast cash campaigns
- Branding, content strategy, or market positioning

**Trigger phrases:** "Hormozi", "Grand Slam Offer", "Value Equation", "100M", "offer stack", "lead generation", "money model", "scaling", "price raise", "lifetime value", "retention", "fast cash", "hook writing", "ad creation"

---

## The 12 Frameworks at a Glance

### 1. Grand Slam Offer
An offer with all four value drivers maximized:
- The Promise — Specific, measurable outcome
- The Mechanism — How you deliver it (unique, proprietary)
- The Price — Relative to value, not cost
- The Guarantee — Risk reversal
- The Scarcity — Real urgency
- The Bonuses — Stack value

**Formula:** Price = 10-25% of total stacked value

### 2. Lead Generation
Get leads so cheap it feels like cheating:
- Content-Market Fit: Match content to market desire
- The Content Matrix: Map content types to funnel stages
- Lead Magnet Architecture: Build magnets that pre-sell

### 3. Money Models
Design revenue architecture that prints cash:
- Front-end: Attraction model (break even or profit)
- Middle: Ascension model (upsells, cross-sells)
- Back-end: High-ticket + Continuity (recurring)

**Formula:** CAC < LTGP (3:1 minimum)

### 4. Scaling Roadmap (10 Stages)

| Stage | Name | Focus | Key Question |
|-------|------|-------|-------------|
| 0 | IMPROVISE | Find what works | "What do people actually want?" |
| 1 | MONETIZE | Make money first | "Will people pay for this?" |
| 2 | ADVERTISE | Get leads profitably | "Can I acquire customers at a profit?" |
| 3 | STABILIZE | Systems & team | "Can this run without me?" |
| 4 | PRIORITIZE | Focus on highest leverage | "What's the one thing that matters most?" |
| 5 | PRODUCTIZE | Package & deliver | "Can I scale delivery?" |
| 6 | OPTIMIZE | Improve margins | "Where am I leaking money?" |
| 7 | CATEGORIZE | Market positioning | "What category do I own?" |
| 8 | SPECIALIZE | Deep expertise | "What am I the best at?" |
| 9 | CAPITALIZE | Exit or hold | "What's my endgame?" |

### 5. Branding
Build a brand that attracts the right people:
- The Bouquet Metaphor: Your brand is a bouquet of associations
- Audience Selection: Pick the pond you want to be the big fish in
- 3 Components: Identity, Association, Reputation

### 6. Fast Cash
Extract cash quickly without damaging long-term value:
- Prepaid Offers: Collect cash before delivering
- Bonus Stacking: Increase perceived value without increasing cost
- Fast Cash Sequence: Email campaign structure

### 7. Hooks
Write hooks that stop the scroll:
- 5 Types: Curiosity, Result, Contrast, Story, Direct
- The Shout Method: How to generate hooks from any content
- Weekly System: 50 hooks → 10 winners → 3 champions

### 8. Lead Nurture
Follow up until they buy or die:
- Speed to Lead: 0-5 min, 5-60 min, 1-24 hr response times
- Multi-Touch Grid: Email, SMS, call, DM sequences
- The Litmus Test: Are you following up enough?

### 9. Lifetime Value
Maximize how much each customer is worth:
- The Crazy Eight: 8 methods to increase LTV
  1. Raise prices
  2. Upsells
  3. Cross-sells
  4. Continuity
  5. Frequency
  6. Reactivation
  7. Referrals
  8. High-ticket backend

### 10. Pricing
Raise prices without losing customers:
- My Rules For Raising Prices: 5 rules
- Price Raise Math: Calculate the impact
- Price Raise Letter: 5-section structure

### 11. Retention
Keep customers longer:
- The 5 Horsemen of Churn: Identify why customers leave
- Churn Checklist: Systematic retention audit
- Perfect Continuity Offer: Design offers that stick

### 12. Advertising
Create ads that scale:
- Hook-Meat-CTA: The 3-part ad structure
- 50 Hooks System: Generate 150-750 ads per week
- Ad Scaling: Kill losers, scale winners

---

## Lost Chapters — Advanced Frameworks

These were "hidden" frameworks from the Lost Chapters book:

### The Three Levers of CFA (Cash Flow Acceleration)
1. **CAC** — Customer Acquisition Cost
2. **LTGP** — Lifetime Gross Profit
3. **PPD** — Profit Per Dollar

### The Value Grid
Map every offer component against:
- High/Low Cost to you
- High/Low Value to customer

**Goal:** Maximize high-value/low-cost components

### Four Steps To Picking
1. List all options
2. Eliminate the worst
3. Compare the rest on one metric
4. Pick the winner and commit

### Four Offer Types
1. **Front-End** — Acquisition
2. **Ascension** — Upsell
3. **Continuity** — Recurring
4. **High-Ticket** — Backend

---

## Usage Examples

### Example 1: Build a Grand Slam Offer

```bash
python3 scripts/apply-framework.py offer "I help busy professionals lose weight"
```

**Output:**
```
=== APPLYING FRAMEWORK: Grand Slam Offer ===

Context: I help busy professionals lose weight

STEP-BY-STEP:
1. Define the dream outcome (what they really want)
   → Look good in a suit, have energy for kids, not think about food

2. Identify current pain (what they're struggling with)
   → No time to meal prep, diets too restrictive, yo-yo results

3. Design the mechanism (your unique method)
   → "The 15-Minute CEO Method" — high-protein meals that take 15 min

4. Stack bonuses (increase perceived value 10x)
   → Bonus 1: Restaurant Survival Guide ($197 value)
   → Bonus 2: Travel Protocol ($297 value)
   → Bonus 3: Spouse Support System ($147 value)

5. Add risk reversal (guarantee)
   → "Lose 10 lbs in 30 days or we work free until you do"

6. Create scarcity (real urgency)
   → Only 5 spots per month for personal accountability

7. Price at 10-25% of total value
   → Total value: $2,941 → Price: $297-497

8. Test with 10 prospects
   → Offer to 10 busy professionals, close 3-5

CHECKLIST:
[✓] Dream outcome is specific and measurable
[✓] Perceived likelihood is high
[✓] Time delay is minimized
[✓] Effort & sacrifice are minimized
[✓] Price is 10-25% of total value
```

### Example 2: Design a Money Model

```bash
python3 scripts/apply-framework.py money-model "Online course business, $100K/year"
```

### Example 3: Write 50 Hooks

```bash
python3 scripts/apply-framework.py hook "Time management for entrepreneurs"
```

---

## File Structure

```
hormozi-100m-frameworks/
├── SKILL.md                          # Master knowledge base (~900 lines)
├── README.md                         # This file
├── scripts/
│   └── apply-framework.py            # CLI tool (11 frameworks)
├── templates/
│   ├── grand-slam-offer.md           # Offer creation template
│   ├── hook-swipe-file.md            # Hook generation template
│   ├── money-model-designer.md       # Revenue architecture template
│   └── scaling-roadmap-checklist.md  # Stage assessment template
└── references/
    ├── framework-index.json          # Machine-readable book index
    └── audit-protocol.md             # Build & verification notes
```

---

## Contributing

This skill was built by extracting frameworks from the complete 100M book series. To contribute:

1. Fork the repo
2. Add your framework or fix
3. Update `framework-index.json` if adding new frameworks
4. Submit a PR

---

## Troubleshooting

### "python3: command not found"
Install Python 3:
```bash
# Ubuntu/Debian
sudo apt-get install python3

# macOS
brew install python3

# Windows
# Download from python.org
```

### "apply-framework.py: permission denied"
Make the script executable:
```bash
chmod +x scripts/apply-framework.py
```

Or run with Python explicitly:
```bash
python3 scripts/apply-framework.py offer "your context here"
```

### "Unknown framework: xyz"
Check the supported frameworks list:
```bash
python3 scripts/apply-framework.py
```

Supported frameworks: `offer`, `money-model`, `hook`, `ad`, `scaling`, `pricing`, `retention`, `branding`, `lifetime-value`, `lead-nurture`, `fast-cash`

### ZIP file won't extract
Make sure you have `unzip` installed:
```bash
# Ubuntu/Debian
sudo apt-get install unzip

# macOS (built-in)
# Windows (built-in in File Explorer)
```

Then extract:
```bash
unzip hormozi-100m-frameworks.zip -d ~/.hermes/skills/hormozi-100m-frameworks
```

### Skill not loading in Hermes Agent
1. Check the skill is in the correct directory:
   ```bash
   ls ~/.hermes/skills/hormozi-100m-frameworks/SKILL.md
   ```
2. Restart your Hermes Agent session
3. Verify the skill YAML frontmatter is valid (first 12 lines of `SKILL.md`)

### Missing a specific framework?
This skill covers the 12 core frameworks. If you need a specific sub-framework:
1. Check `SKILL.md` — many sub-frameworks are embedded within the main sections
2. Check `references/framework-index.json` for the full list of 47 extracted frameworks
3. Open an issue on GitHub with the specific framework name and source book

### Want to use this without Hermes Agent?
You can use this skill standalone:
- Read `SKILL.md` as a reference document
- Use `scripts/apply-framework.py` as a CLI tool
- Use templates in `templates/` as markdown worksheets

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Initial | Basic 8 frameworks |
| 2.0.0 | May 2026 | Complete audit — added Lost Chapters, Scaling details, Crazy Eight, Speed to Lead, Price Raise rules, Fast Cash templates, Retention 5 Horsemen, Shout Method |

---

## Credits

- **Frameworks:** Alex Hormozi — [acq.com](https://acq.com)
- **Skill Author:** alexa
- **Extraction Method:** Python-based text analysis + manual curation
- **Source Material:** 13 books, ~1.2M characters

---

## License

Apache-2.0 — Use freely. Give credit to Hormozi for the frameworks. See [LICENSE](LICENSE) for full terms.

---

> **Note:** This skill contains distilled frameworks and actionable playbooks. It does not contain full book text, copyrighted copy, or proprietary course material. It is a reference tool for applying Hormozi's principles to your own business.
