# Conversion note — Plan 818030JSS (2026-10-29)

`main_floor.scad` on this branch is a conversion of Architectural
Designs **plan 818030JSS, "New American Ranch Plan with Private
Primary Suite — 3564 Sq Ft"**, which Jordan supplied 2026-10-29
(listing PDF + floor-plan image; the image is kept beside this note
as `ranch-plan-818030-source.jpg`). It replaces the previous
main-floor design, which remains on `main` and in git history.

## The plan, from its listing

- 3,564 sq ft heated, 1 storey, 4 bedrooms, 4.5 baths, 3-car garage
  (798 sq ft, side entry — doors face south in this model, as drawn)
- Overall 89'-10" wide × 87'-6" deep, ridge 26'-10", 10 ft ceilings
  (vaults in the game room, primary suite and family room as drawn)
- Standard foundation is a monolithic slab; the plan offers
  **basement / walkout / crawl options** at purchase
- Front porch 169 sq ft, back porch 701 sq ft (with outdoor kitchen
  and fireplace, as drawn)

## How the model was fitted

Rooms are wall-centre-line rectangles in the repo's usual table
format, fitted from the printed room dimensions on the plan image
plus the overall envelope. The marketing image is not perfectly to
scale — a few printed dimensions conflict by 1–3 ft when forced into
one grid (the garage and office are the tightest squeeze) — so the
overall envelope and the labelled bedroom/living sizes won, and the
rest are within about a foot of printed. Treat it like every other
model here: visualisation, not construction documents.

## What this conversion does NOT carry over (needs Jordan's call)

1. **The basement.** `basement.scad` still belongs to the previous
   design (100 × 60 ft, pool/theater/utilities) and does **not**
   align with this footprint — `house_combined.scad` renders, but
   the basement sits wrong under the ranch. Options: buy the plan's
   basement option and model the basement under this footprint,
   adapt the old basement program (pool/theater/utilities) to fit,
   or drop the basement (the ranch is drawn slab-on-grade).
2. **The site model.** `site.scad` (shop v3, west drive, tunnel)
   still places the old house. The shop concept is unaffected, but
   the tunnel's landing was designed for the old basement's
   UTILITIES room; with this plan the house-side utility spaces are
   the mud room + utility/laundry on the east side, and there is no
   basement utility room unless (1) adds one. Re-siting the shop
   against this footprint (garage is now on the south-east, not the
   west) is a follow-up piece of work.
3. **Kayla's changes.** The previous model's review changes
   (bedroom-hall fixes, kitchen work zone, etc.) applied to the old
   plan and are gone with it; this conversion is the plan as drawn.
