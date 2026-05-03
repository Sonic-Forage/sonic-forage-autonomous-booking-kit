#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
required=['README.md','LICENSE','.env.example','docs/booking/AUTONOMOUS_BOOKING_AGENT_PLAN.md','docs/booking/HUMAN_APPROVAL_LEDGER.md','docs/booking/BOOKING_ONE_SHEET_TEMPLATE.md','docs/booking/BOOKING_ONE_SHEET_DRAFT_EXAMPLE.md','docs/booking/ASSET_ATTACHMENT_APPROVAL_CHECKLIST.md','framework/prompts/booking-agent-prompts.md','framework/payloads/booking-lead.payload.example.json','framework/payloads/booking-campaign.payload.example.json','framework/tags/booking-tags.json','docs/index.html']
missing=[p for p in required if not (ROOT/p).exists()]
if missing: print('MISSING:', *missing, sep='\n- '); sys.exit(1)
for rel in ['framework/payloads/booking-lead.payload.example.json','framework/payloads/booking-campaign.payload.example.json','framework/tags/booking-tags.json']:
    json.loads((ROOT/rel).read_text())
campaign=json.loads((ROOT/'framework/payloads/booking-campaign.payload.example.json').read_text())
fail_closed={
    'asset_attachment_policy':'closed_until_human_yes',
    'raw_media_attachment_allowed':False,
    'private_media_link_allowed':False,
    'payment_link_allowed':False,
    'requires_human_approval':True,
}
for key, expected in fail_closed.items():
    if campaign.get(key) != expected:
        print('UNSAFE CAMPAIGN FIELD', key); sys.exit(1)
if not isinstance(campaign.get('selected_public_asset_paths'), list):
    print('CAMPAIGN ASSET PATHS MUST BE LIST'); sys.exit(1)
if not campaign.get('selected_public_asset_paths'):
    print('CAMPAIGN NEEDS PUBLIC ASSET PATH EXAMPLES'); sys.exit(1)
for asset_path in campaign['selected_public_asset_paths']:
    if not isinstance(asset_path, str) or asset_path.startswith(('/', 'http://', 'https://')):
        print('UNSAFE CAMPAIGN ASSET PATH', asset_path); sys.exit(1)
    if Path(asset_path).suffix.lower() in {'.wav','.mp3','.flac','.m4a','.mp4','.mov','.webm'}:
        print('RAW MEDIA PATH IN CAMPAIGN ASSET LIST', asset_path); sys.exit(1)
if campaign.get('one_sheet_draft_example') != 'docs/booking/BOOKING_ONE_SHEET_DRAFT_EXAMPLE.md':
    print('MISSING ONE-SHEET DRAFT EXAMPLE POINTER'); sys.exit(1)
if campaign.get('asset_vault_public_promo_selector') != 'asset-library/public-promo-selection-manifest.json':
    print('MISSING PUBLIC PROMO SELECTOR POINTER'); sys.exit(1)
text='\n'.join((ROOT/p).read_text(errors='replace') for p in required)
for needle in ['closed_until_human_yes','Do not send','human approval','not autonomous spam','Asset vault']:
    if needle.lower() not in text.lower(): print('MISSING NEEDLE', needle); sys.exit(1)
if re.search(r'(ghp_|github_pat_|sk-[A-Za-z0-9]|hf_[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY)', text): print('SECRET-LIKE MARKER'); sys.exit(1)
if re.search(r'will send automatically|autonomous spam|guaranteed booking|payment link live', text, re.I) and 'not autonomous spam' not in text.lower(): print('UNSAFE BOOKING CLAIM'); sys.exit(1)
print('BOOKING KIT VERIFY OK')
print('required files:', len(required))
