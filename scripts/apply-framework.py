#!/usr/bin/env python3
"""
Hormozi $100M Frameworks - Application Script v2
Usage: python apply-framework.py <framework> <context>

Frameworks: offer, money-model, hook, ad, scaling, pricing, retention, branding,
            lifetime-value, lead-nurture, fast-cash
"""

import sys, json, os

FRAMEWORKS = {
    "offer": {
        "name": "Grand Slam Offer",
        "steps": [
            "Define the dream outcome (what they really want)",
            "Identify current pain (what they're struggling with)",
            "Design the mechanism (your unique method)",
            "Stack bonuses (increase perceived value 10x)",
            "Add risk reversal (guarantee)",
            "Create scarcity (real urgency)",
            "Price at 10-25% of total value",
            "Test with 10 prospects"
        ],
        "checklist": [
            "Dream outcome is specific and measurable",
            "Perceived likelihood is high",
            "Time delay is minimized",
            "Effort & sacrifice are minimized",
            "Price is 10-25% of total value"
        ]
    },
    "money-model": {
        "name": "Money Model Design",
        "steps": [
            "Map current revenue streams",
            "Identify the bottleneck",
            "Design front-end offer (attraction)",
            "Build upsell sequence (ascension)",
            "Add continuity layer (recurring)",
            "Calculate unit economics (CAC, LTGP, margin)",
            "Test funnel with paid traffic",
            "Optimize weakest link"
        ],
        "checklist": [
            "CAC < LTGP (3:1 minimum)",
            "Front-end breaks even or profits",
            "Upsell sequence increases AOV 2x+",
            "Continuity layer exists",
            "High-ticket backend exists"
        ]
    },
    "hook": {
        "name": "Hook Writing",
        "steps": [
            "Identify audience's #1 desire",
            "Identify their #1 fear/frustration",
            "Choose hook type (curiosity, result, contrast, story, direct)",
            "Write 50 variations",
            "Test top 10 with small budget",
            "Measure CTR and engagement",
            "Double down on winners"
        ],
        "templates": [
            "How I [result] in [timeframe] without [sacrifice]",
            "What [authority] doesn't want you to know about [topic]",
            "Why most [audience] will never [outcome]",
            "I was [negative] until I discovered [mechanism]",
            "Want [outcome]? Read this."
        ]
    },
    "ad": {
        "name": "GOATed Ad Creation",
        "steps": [
            "Write 50 hooks",
            "Create 3-5 meat variations per hook",
            "Add 1-3 CTAs per variation",
            "Build 150-750 ad combinations",
            "Launch test campaign",
            "Kill losers, scale winners",
            "Refresh creative weekly"
        ],
        "structure": {
            "hook": "First 3 seconds - stop the scroll",
            "meat": "Middle - deliver value, build trust",
            "cta": "End - clear next step"
        }
    },
    "scaling": {
        "name": "10-Stage Scaling",
        "stages": [
            "0. IMPROVISE - Find what works",
            "1. MONETIZE - Make money first",
            "2. ADVERTISE - Get leads profitably",
            "3. STABILIZE - Systems & team",
            "4. PRIORITIZE - Focus on leverage",
            "5. PRODUCTIZE - Package & deliver",
            "6. OPTIMIZE - Improve margins",
            "7. CATEGORIZE - Own a category",
            "8. SPECIALIZE - Deep expertise",
            "9. CAPITALIZE - Exit or hold"
        ]
    },
    "pricing": {
        "name": "Price Raise Strategy",
        "steps": [
            "Document current value delivered",
            "List improvements made",
            "Justify the increase",
            "Set new price with timeline",
            "Create grandfather option",
            "Send price raise email/letter",
            "Handle objections",
            "Measure churn impact"
        ],
        "rules": [
            "Pair with a launch (within 90 days)",
            "Add value first",
            "Communicate clearly",
            "Grandfather existing customers",
            "Test on new customers first"
        ]
    },
    "retention": {
        "name": "The 5 Horsemen of Retention",
        "horsemen": [
            "Results - Do customers get what they paid for?",
            "Engagement - Are they actively using/participating?",
            "Community - Do they feel belonging?",
            "Progress - Can they see improvement?",
            "Surprise - Do you exceed expectations?"
        ]
    },
    "branding": {
        "name": "Brand Building",
        "steps": [
            "Define what you say (advertising)",
            "Define what you do (actions)",
            "Define what others say (reputation)",
            "Select growing audience with money",
            "Ensure audience is easy to target",
            "Confirm audience is in pain",
            "Build consistent brand experience"
        ]
    },
    "lifetime-value": {
        "name": "LTV Maximization (The Crazy Eight)",
        "methods": [
            "Increase Prices",
            "Decrease Costs",
            "Increase # of Purchases",
            "Cross-Sell Something Different",
            "Sell More (Increase Quantity)",
            "Sell Better (Increase Quality)",
            "Downsell Fewer (Lower Quantity)",
            "Downsell Lower Quality"
        ]
    },
    "lead-nurture": {
        "name": "Lead Nurture System",
        "speeds": [
            "Speed To First Contact - Contact in 5 min or less",
            "Speed To First Appointment - Same/next day",
            "Speed Of Response - Reply in minutes"
        ],
        "sequence": [
            "Immediate (0-5 min): Text response",
            "Same Day: Email + phone call",
            "Day 2-3: Follow up with value",
            "Day 4-7: Personal check-in",
            "Week 2+: Weekly touches"
        ]
    },
    "fast-cash": {
        "name": "Fast Cash Campaign",
        "sequence": [
            "7 Days Out: Tease something big",
            "5 Days Out: Announce offer",
            "3 Days Out: Reveal bonuses",
            "Day Of: Cart open",
            "12 Hours: Final warning",
            "1 Hour: Cart closing"
        ]
    }
}

def apply_framework(framework_name, context=""):
    framework = FRAMEWORKS.get(framework_name.lower())
    if not framework:
        print(f"Unknown framework: {framework_name}")
        print(f"Available: {', '.join(FRAMEWORKS.keys())}")
        return
    
    print(f"\n{'='*60}")
    print(f"APPLYING: {framework['name']}")
    print(f"{'='*60}")
    
    if context:
        print(f"\nCONTEXT: {context}")
    
    if 'steps' in framework:
        print(f"\nSTEPS:")
        for i, step in enumerate(framework['steps'], 1):
            print(f"  {i}. {step}")
    
    if 'checklist' in framework:
        print(f"\nCHECKLIST:")
        for item in framework['checklist']:
            print(f"  [ ] {item}")
    
    if 'templates' in framework:
        print(f"\nTEMPLATES:")
        for template in framework['templates']:
            print(f"  • {template}")
    
    if 'horsemen' in framework:
        print(f"\nTHE 5 HORSEMEN:")
        for horseman in framework['horsemen']:
            print(f"  • {horseman}")
    
    if 'stages' in framework:
        print(f"\nSTAGES:")
        for stage in framework['stages']:
            print(f"  • {stage}")
    
    if 'structure' in framework:
        print(f"\nSTRUCTURE:")
        for key, value in framework['structure'].items():
            print(f"  {key.upper()}: {value}")
    
    if 'rules' in framework:
        print(f"\nRULES:")
        for rule in framework['rules']:
            print(f"  • {rule}")
    
    if 'methods' in framework:
        print(f"\nMETHODS:")
        for method in framework['methods']:
            print(f"  • {method}")
    
    if 'speeds' in framework:
        print(f"\nTHE 3 SPEEDS:")
        for speed in framework['speeds']:
            print(f"  • {speed}")
    
    if 'sequence' in framework:
        print(f"\nSEQUENCE:")
        for step in framework['sequence']:
            print(f"  • {step}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python apply-framework.py <framework> [context]")
        print(f"Frameworks: {', '.join(FRAMEWORKS.keys())}")
        sys.exit(1)
    
    framework = sys.argv[1]
    context = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
    apply_framework(framework, context)
