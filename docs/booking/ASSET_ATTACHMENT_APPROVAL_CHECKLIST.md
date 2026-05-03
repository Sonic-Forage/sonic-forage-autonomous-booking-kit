# Asset Attachment Approval Checklist

Status: `closed_until_human_yes`

This checklist turns the Sonic Forage asset vault into a safe booking-kit handoff without sending, uploading, copying, or attaching raw media automatically. It is review-only until an awake operator approves the exact target, copy, links, and attachments.

## Default rule

Do not send outreach, DMs, emails, calendar invites, booking pitches, payment links, public posts, media attachments, or private asset links without human approval.

Use the public asset vault as an index and one-sheet source only:

- Canonical asset vault: https://github.com/Sonic-Forage/sonic-forage-asset-vault
- Public-safe promo catalog: `asset-library/promo-asset-catalog.json`
- Raw-media storage policy: `docs/media/MEDIA_STORAGE_POLICY.md`
- Release approval checklist: `docs/media/RELEASE_APPROVAL_CHECKLIST.md`

## Attachment decision slots

| Slot | Default state | Human must approve | Blocked without approval |
| --- | --- | --- | --- |
| Public repo link | `closed_until_human_yes` | Target-specific fit, context, and copy | Sending link in outreach |
| Small promo image | `closed_until_human_yes` | Exact image, license posture, alt text, and recipient | Attaching or embedding image |
| Raw track/audio | `closed_until_human_yes` | Rights, recipient, storage location, retention, and takedown path | Uploading, copying, attaching, streaming, or publishing raw media |
| Private media folder | `closed_until_human_yes` | Access list, expiry, revocation path, and privacy notes | Sharing private-drive/object-store links |
| Payment/booking CTA | `closed_until_human_yes` | Offer, price, terms, payment processor, and refund language | Sending payment links or contract commitments |

## Operator flow

1. Run `python3 scripts/verify.py` in this booking-kit repo.
2. Open the asset vault manifest and choose only public-safe, small promo assets by repo-relative path.
3. Draft the one-sheet in `docs/booking/BOOKING_ONE_SHEET_TEMPLATE.md` or a target-specific copy outside git.
4. Fill the manual human approval ledger in `docs/booking/HUMAN_APPROVAL_LEDGER.md` with the exact target, copy, timing, and selected assets.
5. Stop. The send remains blocked until the human explicitly says yes.

## Safe payload fields

When creating a draft payload, keep these fields explicit and closed:

```json
{
  "asset_attachment_policy": "closed_until_human_yes",
  "selected_public_asset_paths": [],
  "raw_media_attachment_allowed": false,
  "private_media_link_allowed": false,
  "payment_link_allowed": false,
  "requires_human_approval": true
}
```

## Acceptance checks

- `closed_until_human_yes` appears in every attachment lane.
- `requires_human_approval` is true before any target-specific send.
- Raw media is not committed, uploaded, migrated, copied, attached, or published by this kit.
- The booking agent prepares drafts only; it is not autonomous spam.
