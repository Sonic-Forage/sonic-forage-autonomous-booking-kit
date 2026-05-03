# 🤖 Sonic Forage Autonomous Booking Kit

Open-source, closed-gate framework for an AI-assisted booking/PR/operator agent for DJs, community shows, educational workshops, and Sonic-Forage demos.

This is **not** an unsupervised spam bot. It prepares booking assets, CRM-style research, pitch drafts, approval ledgers, and follow-up tasks. Humans approve every external send.

## What it does safely

- build booking one-sheets
- assemble asset links
- draft venue/festival/community emails
- classify leads as `research_only`, `warm_intro`, or `do_not_contact`
- prepare call sheets and follow-up checklists
- keep every outreach/payment/public action closed until human approval

## Key files

- `docs/booking/AUTONOMOUS_BOOKING_AGENT_PLAN.md`
- `docs/booking/HUMAN_APPROVAL_LEDGER.md`
- `docs/booking/BOOKING_ONE_SHEET_TEMPLATE.md`
- `docs/booking/ASSET_ATTACHMENT_APPROVAL_CHECKLIST.md`
- `framework/prompts/booking-agent-prompts.md`
- `framework/payloads/booking-lead.payload.example.json`
- `framework/payloads/booking-campaign.payload.example.json`
- `framework/tags/booking-tags.json`
- `scripts/verify.py`

## Linked assets

Asset vault: https://github.com/Sonic-Forage/sonic-forage-asset-vault

## Default state

`closed_until_human_yes`
