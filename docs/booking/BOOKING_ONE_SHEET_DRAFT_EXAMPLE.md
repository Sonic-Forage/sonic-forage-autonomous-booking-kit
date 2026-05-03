# Booking One-Sheet Draft Example

Status: `closed_until_human_yes`

This is a local, review-only example of how the booking kit can assemble a one-sheet using public asset-vault references. It is not an email, DM, calendar invite, pitch send, payment request, public post, or media attachment authorization.

## Draft target placeholder

- Target / venue / partner: `<human-selected-target>`
- Contact channel: `<human-selected-channel>`
- Proposed timing: `<human-approved-window>`
- Offer terms: `<human-approved-copy>` only
- Risk notes: `<human-reviewed-context>`

## Public-safe asset references

Use these as visible links or preview images only after a human approves the exact target, copy, timing, and attachment list:

| Use | Asset-vault path | Status |
| --- | --- | --- |
| Square promo preview | `assets/images/promo/asset-vault-square-promo.png` | committed public generated promo asset |
| Community framework banner | `assets/images/banners/sonic-forage-community-framework-banner.png` | committed public generated promo asset |
| Booking-agent banner | `assets/images/banners/autonomous-booking-agent-banner.png` | committed public generated promo asset |

Raw tracks, audio stems, video, private source media, private drive links, signed URLs, and unpublished folders remain blocked. The asset vault is manifest-based; raw media is indexed but not committed.

## Draft one-sheet copy block

> Sonic Forage is an open-source creative-tech and rave-community toolkit: a manifest-based public asset vault, safer dance-space field-guide lane, and autonomous booking prep kit. This draft can help a human operator prepare a venue/community partner conversation with public promo images and repo links only. It does **not** send automatically, attach raw media, create payment links, or claim confirmed availability.

## Required human approval before any external action

The operator must answer and log all of the following in `docs/booking/HUMAN_APPROVAL_LEDGER.md` before any send or attachment:

1. Which target is approved?
2. Which exact copy is approved?
3. Which public asset paths are approved?
4. Are raw/private media links still excluded? Expected answer: yes.
5. Is a payment link, contract, invoice, public post, calendar invite, or private media upload involved? Expected answer for this draft: no.

Blocked without approval: outreach send, DMs, email, calendar invites, booking pitches, payment links, public posts, raw media attachments, private media links, source-media folder sharing, dataset upload/training, GPU/video generation, and cron changes.

## Payload alignment

The companion campaign payload keeps the same gate:

- `asset_attachment_policy: closed_until_human_yes`
- `raw_media_attachment_allowed: false`
- `private_media_link_allowed: false`
- `payment_link_allowed: false`
- `requires_human_approval: true`

This example is suitable for local review and GitHub Pages copy only; it is not autonomous spam and it does not open an external lane.
