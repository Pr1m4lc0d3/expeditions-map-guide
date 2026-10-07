---
title: Store and garage artwork
part: Vehicles
order: 660
summary: Every image a vehicle needs, what size it is, which one must be a cut-out, and the one pair you must never give a vehicle of its own.
---

# Store and garage artwork

A vehicle can render perfectly, drive perfectly, and still look like someone
else's truck everywhere the UI shows a picture of it. None of these fields logs
anything when it is wrong, so the only way to find a mistake is to open the
store and look.

## The fields

<span class="prov prov-unver">measured across the game's 44 stock truck classes</span>

| field | size | kind | where it shows | stock trucks declaring it |
|---|---|---|---|---|
| `TruckImage` | 380×110 | **cut-out, RGBA** | the card in the truck list | 44 / 44 |
| `TruckImageSmall` | 124×52 | **cut-out, RGBA** | compact list variant | 1 / 44 |
| `UiIcon328x458` | 328×458 | scene photo | store list thumbnail | 42 / 44 |
| `UiIcon576x640` | 576×640 | scene photo | large store preview | 43 / 44 |
| `uiIcon576x640Bw` | 576×640 | scene photo, greyscale | greyscale variant | 1 / 44 |
| `UiIconLogo` | 80×80 | badge | manufacturer badge | 42 / 44 |
| `UiIcon40x40` | — | **shared glyph** | fleet tab, top of truck selection | 44 / 44 |
| `UiIcon30x30` | — | **shared glyph** | fleet tab, small | 44 / 44 |

`TruckImage*` live in `<TruckData>`. The `UiIcon*` live in `<UiDesc>`.

Note that `UiIcon328x458` is **absent from the editor's type schema** and is used
by 42 of the 44 shipped trucks. Schema absence is not invalidity — check what the
game's own content does before concluding a field is wrong.

## The two rules that cost the most

### A cut-out slot needs alpha, and an opaque screenshot renders as nothing

`TruckImage` and `TruckImageSmall` are composited into the UI. They must be RGBA
with the vehicle isolated on transparency. Put a rectangle of garage scene in
one of those slots and the card is simply blank — no error, no fallback.

The store slots are the opposite: they are ordinary opaque photographs, exactly
like every stock truck's.

### The fleet tabs are shared, and giving a vehicle its own empties them

!!! danger "Never point `UiIcon40x40` / `UiIcon30x30` at a per-vehicle image"
    All 44 stock trucks point these at a **shared category glyph** —
    `scoutVehicleImg` ×27, `offroadVehicleImg` ×13, `heavyVehicleImg` ×2 — and so
    does every working mod. Those names resolve and draw the little grey truck
    icon you see in the tabs.

    Repointing them at a unique name and shipping the PNG produces an **empty
    tab**. The other image fields do resolve shipped files; these two do not.

    Inherit the glyph for your vehicle's category and leave the fields alone.

## Composing the shot

```
python F:\Expeditions\Toolkit\vehicle_ui.py --howto
```

That prints the whole recipe. In short:

* **Three-quarter front**, roughly 30–45° off the nose. Every stock card and
  every working mod uses that angle.
* **Fill the frame.** You cannot zoom in afterwards without losing resolution.
* Keep the vehicle clear of the left-hand truck list and the bottom-right button
  row.
* The Customize screen (`F`) is often better lit and has no stats panel over the
  scene.

Then:

```
python vehicle_ui.py mod.pak out.pak --shot shot.png --name Tundra \
    --box 1500 760 3830 2010 --safe 1560 330 3830 1808 --badge TRD
```

`--box` only has to **contain** the vehicle — the tool mattes it and measures the
real silhouette, so a generous box is safe and a tight one is not. Too small is
the only real mistake: it clips the roof or the bed, and nothing tells you.

!!! warning "`--safe` is per-shot, and it is where the HUD gets baked in"
    The store portraits are cropped from the scene, so any button or label
    inside `--safe` ends up in the artwork. Where the HUD sits *relative to the
    vehicle* changes per truck: a long-nosed truck reaches under the `M Map`
    row, so you crop above it; a short one does not, so you cut the right edge
    instead. Decide it from your own screenshot.

!!! note "A scene object touching the bodywork survives the matte"
    A crate or post standing against the vehicle shares an edge with it, so
    neither the matte nor a largest-blob filter can tell them apart —
    morphological opening does not sever it either. Paint it out at source with
    `--exclude L T R B`, which is repeatable.

## Matching the stock cards

<span class="prov prov-unver">measured</span>
Stock cards are **zoomed in far enough to crop at the bumper**. Fitting the whole
vehicle inside the frame is the obvious thing to do and it looks visibly small
next to them.

The only readable reference is a mod that ships real files instead of inheriting
atlas sprites. Its card:

| | |
|---|---|
| canvas | 380×110 |
| content width | 50% of the canvas, left-aligned |
| vertical | **touches both top and bottom** — the vehicle overflows |
| bottom row | 109 of 380 pixels filled, i.e. cut straight through the wheels |

That works out to drawing the vehicle about **1.5 frame-heights tall**, anchored
left and centred vertically so it crops evenly at the roof and the bumper. The
toolkit does this by default; `cutout(..., fill=1.5)` is the knob.

Stock `TruckImage` names such as `don71mchr` are **atlas sprites and exist
nowhere as files**, so you cannot open one to compare. A mod that ships its own
PNG is the only ground truth available.
