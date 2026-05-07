# Skill Audit & Enhancement Protocol

This document captures the methodology used to audit and expand this skill from v1.0 → v2.0. Use it when adding new books or frameworks.

## When to Audit

- User says "audit and add missing parts"
- New book/source material is discovered
- Skill feels incomplete for a specific use case
- A framework is mentioned that isn't in the skill

## The Audit Process

### Step 1: Inventory Source Files

Locate all source files (PDFs, TXTs, etc.). In this session:
```bash
ls -la /root/Downloads/100M/txt/
```

### Step 2: Extract Structure

Use Python to find patterns Hormozi uses:

```python
import os, re

# Patterns to extract:
- Numbered lists: r'^\d+\.\s+([A-Z][^\n]{10,200})'
- Bullet lists: r'^[-•○\*]\s+'
- Section headers (ALL CAPS, short)
- "The X" frameworks: r'^The\s+[A-Z][a-zA-Z\s]{3,60}'
- Scenarios: r'^(If\s+you|When\s+you|Say\s+you|Imagine)'
- Questions: lines with ? and 15-200 chars
- Rules: r'^(Rule|My\s+Rule|The\s+Rule)'
- Formulas with = and numbers
- Examples: r'^(Ex\.?|Example[:\-])'
```

### Step 3: Identify Gaps

Compare extracted frameworks against SKILL.md sections:
- Does each book have a dedicated section?
- Are formulas extracted and documented?
- Are email templates captured?
- Are sequences/timelines documented?
- Are decision frameworks included?

### Step 4: Deep Dive on High-Value Sections

For the largest/most important source files, extract specific content:
- Read sections by index (e.g., `content[idx:idx+5000]`)
- Capture first 20-30 lines of each section
- Note chapter titles, section headers, key lists

### Step 5: Update SKILL.md

Add missing frameworks as new subsections. Follow the existing pattern:
- Section header (##)
- Concept explanation
- Formula/code block if applicable
- Example if available
- Actionable checklist/steps

### Step 6: Update Support Files

- `references/framework-index.json` — Add new books/frameworks
- `scripts/apply-framework.py` — Add new framework to FRAMEWORKS dict
- `templates/` — Create new templates if needed

### Step 7: Test

Run the script to verify:
```bash
python3 scripts/apply-framework.py <new-framework> "test context"
```

### Step 8: Version Bump

Update version in SKILL.md frontmatter:
```yaml
version: X.Y.Z
```

## Extraction Patterns That Worked

**Hormozi's Signature Patterns:**
- "The [Noun]" — The Value Equation, The Bouquet Metaphor, The Crazy Eight
- "[Number] [Things]" — The Four Offer Types, The Three Levers, The 5 Horsemen
- "How to [Verb]" — How to Calculate LTV, How to Pick Your Price
- "My Rules For [Topic]" — My Rules For Raising Prices
- "The [Adjective] [Noun]" — The Perfect Price Raise, The Grand Slam Offer
- Numbered steps with capital letters: "1. Do This Thing"
- Dollar amounts with math: "$100 - $20 = $80"

**What NOT to Extract:**
- Copyright/disclaimer text
- Marketing CTAs ("Book a call at...")
- Table of contents lines without content
- Individual story details (extract the framework, not the narrative)
- One-off examples (extract the pattern)

## Common Gaps Found in v1.0 → v2.0

1. **Lost Chapters** was severely under-represented (largest book, most frameworks)
2. Email templates from Fast Cash were missing entirely
3. Price raise letter structure (physical mail) was missing
4. Speed to Lead had no sequence/timing details
5. The Crazy Eight had no explanation
6. Hook types were under-categorized
7. Branding had no expansion/contraction guidance
8. Retention math was missing

## Lessons Learned

- The biggest book (Lost Chapters) contained the most missing frameworks
- Hormozi repeats frameworks across books — deduplicate but note variations
- Formulas are scattered — aggregate them in one place
- Email templates are worth extracting verbatim (with placeholders)
- Decision frameworks (questions to ask) are as valuable as formulas
- Always test the script after adding new frameworks
