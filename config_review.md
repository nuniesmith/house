# Floor Plan Config YAML — Review & Improvement Areas

After comparing the output images against `config/floorplan.yaml` and the codebase, here's a breakdown of what needs attention.

---

## Main Floor Plan

### 1. Missing Pool-of-Water Object in Basement `pool:` Section
**Priority: High**

The `pool:` config currently has a zeroed-out structure with no actual pool rectangle defined:

```yaml
pool:
    area:
        x: 0
        y: 0
        width: 25
        height: 35
        color: pool_area
        label: ""
    hot_tub:
        x: 10
        y: 10
        radius: 0        # ← radius is 0, so nothing draws
        color: spa
        edge_color: "#0288d1"
        label: ""
    spa_label:
        x: 0
        y: 0
        text: ""
```

The image shows a blue pool rectangle inside the aqua pool area, but the config is missing a `pool` (water) sub-key entirely. The code in `generators.py` looks for `pool_config.get("pool", pool_config.get("pool_water", {}))` but finds nothing. The hot tub radius is `0`, so it's also skipped.

**Fix:** Add the inner pool and hot tub config:
```yaml
pool:
    area:
        x: 0
        y: 0
        width: 25
        height: 35
        color: pool_area
        label: "POOL / HOT TUB"
    pool:                          # ← ADD THIS
        x: 5
        y: 3
        width: 12
        height: 22
        color: pool
        edge_color: "#0288d1"
        label: "Salt Water\nPool"
    hot_tub:
        x: 8
        y: 27
        radius: 4                  # ← Set actual radius
        color: spa
        edge_color: "#0288d1"
        label: "Hot\nTub"
```

---

### 2. Empty Theater Seating Array
**Priority: Medium**

```yaml
theater:
    room:
        x: 0
        y: 35
        ...
    seating: []    # ← Empty, no chairs drawn
```

The Home Theater room renders, but there's no seating furniture. The code supports `TheaterSeating` with rows, seats per row, spacing, etc.

**Fix:**
```yaml
theater:
    room:
        x: 0
        y: 35
        width: 30
        height: 25
        label: "Home Theater"
        color: theater
        label_fontsize: 12
    seating:
        start_x: 3
        start_y: 37
        rows: 3
        seats_per_row: 5
        chair_width: 3
        chair_height: 2.5
        row_spacing: 5
        seat_spacing: 4
        chair_color: chair
        edge_color: gray
    false_wall:
        x1: 0
        y1: 35
        x2: 30
        y2: 35
        color: red
        linewidth: 4
        linestyle: "--"
        label: "False Wall"
        label_x: 15
        label_y: 33
```

---

### 3. Butler's Pantry Width Gap
**Priority: Medium**

The Dining Room is 18' wide (`x: 43, width: 18` → ends at x=61), but the Butler's Pantry above it is only 16' wide (`x: 43, width: 16` → ends at x=59). This creates a 2' unaccounted gap between x=59 and x=61 at y=15–25.

**Fix:** Either widen Butler's Pantry to 18' to match, or add a small utility/passage room to fill the gap.

```yaml
# Option A: Match dining room width
- x: 43
  y: 15
  width: 18    # was 16
  height: 10
  label: "BUTLER'S\nPANTRY"
  color: utility
```

---

### 4. Missing Stairs (Both Floors)
**Priority: High**

Both `main_floor.stairs` and `basement.stairs` are empty arrays (`[]`). There's no stairway connecting the two floors. The basement has "STAIRS UP" and "EXIT STAIRS" as room boxes with solid fills, but no actual stair-step rendering (the code's `draw_stairs_from_data` function draws treads and labels like "DN"/"UP").

In the output images, these areas show as flat colored rectangles instead of proper stair graphics.

**Fix for main floor** (add stairs to basement):
```yaml
stairs:
    - x: 70
      y: 15
      width: 12
      height: 6
      num_steps: 10
      orientation: horizontal
      label: "DN"
```

**Fix for basement:**
```yaml
stairs:
    - x: 72
      y: 47
      width: 16
      height: 12
      num_steps: 12
      orientation: vertical
      label: "UP"
    - x: 92
      y: 10
      width: 6
      height: 40
      num_steps: 20
      orientation: vertical
      label: "EXIT"
```

---

### 5. No Fireplaces Defined
**Priority: Low**

`main_floor.fireplaces: []` — For a house this size with a Family Room and Lounge, a fireplace would be typical. The drawing code fully supports it.

```yaml
fireplaces:
    - x: 75
      y: 25
      width: 4
      height: 3
      label: "Gas Fireplace"
```

---

### 6. Sparse Window Coverage
**Priority: Medium**

Only 6 windows are defined for a ~125' × 70' home. Most bedrooms, the Master Suite, Lounge rear wall, and Kitchen side walls have no windows. The output image shows very few window markers.

**Suggested additions:**
```yaml
windows:
    # ... existing 6 ...
    # Bedroom 2 (north wall)
    - x: 30
      y: 72
      width: 6
      orientation: horizontal
    # Bedroom 3 (west wall)
    - x: 25
      y: 48
      width: 5
      orientation: vertical
    # Bedroom 4 (west wall)
    - x: 25
      y: 28
      width: 5
      orientation: vertical
    # Master Suite (south wall)
    - x: 92
      y: 0
      width: 8
      orientation: horizontal
    # Lounge (rear/north wall)
    - x: 77
      y: 15
      width: 6
      orientation: horizontal
    # Kitchen (west-ish wall toward bedrooms)
    - x: 43
      y: 35
      width: 5
      orientation: vertical
```

---

### 7. Incomplete Door Coverage
**Priority: Medium**

8 doors defined for 15+ rooms. Missing doors include: Laundry, Butler's Pantry to Kitchen, Kitchen to Family Room, Lounge entry, Dining Room entry, Master Bath, WIC, and exterior/patio doors (Outdoor Living, Front Porch side entries).

---

### 8. Empty Furniture Arrays (Both Floors)
**Priority: Low**

`main_floor.furniture: []` and `basement.furniture: []`. No kitchen islands, bathroom fixtures, closet shelving, bar counters, or pool deck furniture. The Bar room in the basement is defined as a colored rectangle room, but a furniture-based bar counter would be more representative.

---

### 9. Basement Label Inconsistency
**Priority: Low**

The config defines `label: "STAIRS EXIT"` but the output image reads "EXIT STAIRS". Verify which label you want and make them consistent. The room label in the YAML is what gets rendered.

---

### 10. Outdoor Living / Porch Alignment
**Priority: Low**

The Outdoor Living porch (`x: 45, y: 43, width: 40`) extends to x=85, but the Family Room extends to x=87 and the Kitchen starts at x=43. The porch should probably start at x=43 (matching the Kitchen) and extend to x=87 (matching the Family Room edge) for a width of 44':

```yaml
- x: 43
  y: 43
  width: 44    # was 40, starting at x=45
  height: 15
  label: "OUTDOOR\nLIVING"
  color: porch
```

Or if intentionally offset, add a comment explaining why.

---

### 11. Basement Room Overlap: Open Rec Area Extends Behind Stairs/Utilities
**Priority: Low**

The Open Rec Area (`x: 25, y: 20, width: 65, height: 25` → extends to x=90, y=45) overlaps visually with the Utilities room (`x: 30, y: 45`) and Stairs Up (`x: 70, y: 45`) at the y=45 boundary, and with the Exit Stairs (`x: 90, y: 0, height: 60`) at the x=90 boundary. The rendering handles z-order so later rooms draw on top, but it's not clean architecturally. Consider trimming the Rec Area width to 65 from x=25 → x=90 or adjusting to avoid the exit stairs column.

---

## Summary Table

| # | Issue | Floor | Priority | Type |
|---|-------|-------|----------|------|
| 1 | Pool water rect & hot tub missing | Basement | High | Missing config |
| 2 | Theater seating empty | Basement | Medium | Missing config |
| 3 | Butler's Pantry width gap | Main | Medium | Coordinate fix |
| 4 | No stairs defined | Both | High | Missing config |
| 5 | No fireplaces | Main | Low | Missing config |
| 6 | Sparse windows (6 total) | Main | Medium | Missing config |
| 7 | Incomplete doors | Main | Medium | Missing config |
| 8 | Empty furniture arrays | Both | Low | Missing config |
| 9 | "STAIRS EXIT" vs "EXIT STAIRS" | Basement | Low | Label fix |
| 10 | Outdoor Living offset | Main | Low | Coordinate fix |
| 11 | Rec Area overlaps Exit Stairs | Basement | Low | Coordinate fix |
