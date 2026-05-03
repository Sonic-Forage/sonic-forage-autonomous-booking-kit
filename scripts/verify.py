#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
required=['README.md','LICENSE','.env.example','docs/booking/AUTONOMOUS_BOOKING_AGENT_PLAN.md','docs/booking/HUMAN_APPROVAL_LEDGER.md','docs/booking/BOOKING_ONE_SHEET_TEMPLATE.md','framework/prompts/booking-agent-prompts.md','framework/payloads/booking-lead.payload.example.json','framework/payloads/booking-campaign.payload.example.json','framework/tags/booking-tags.json','docs/index.html']
missing=[p for p in required if not (ROOT/p).exists()]
if missing: print('MISSING:', *missing, sep='\n- '); sys.exit(1)
for rel in ['framework/payloads/booking-lead.payload.example.json','framework/payloads/booking-campaign.payload.example.json','framework/tags/booking-tags.json']:
    json.loads((ROOT/rel).read_text())
text='\n'.join((ROOT/p).read_text(errors='replace') for p in required)
for needle in ['closed_until_human_yes','Do not send','human approval','not autonomous spam','Asset vault']:
    if needle.lower() not in text.lower(): print('MISSING NEEDLE', needle); sys.exit(1)
if re.search(r'(ghp_|github_pat_|sk-[A-Za-z0-9]|hf_[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY)', text): print('SECRET-LIKE MARKER'); sys.exit(1)
if re.search(r'will send automatically|autonomous spam|guaranteed booking|payment link live', text, re.I) and 'not autonomous spam' not in text.lower(): print('UNSAFE BOOKING CLAIM'); sys.exit(1)
print('BOOKING KIT VERIFY OK')
print('required files:', len(required))
