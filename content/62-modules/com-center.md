---
title: Intelligence center
part: Appendix A - base modules
order: 910
summary: Extends the signal radius around the base. Documented for custom modules.
verdict: broken
verdict_text: "It builds, sells and pays its refund, but it never marks a single air drop, even with the game's own script patched. Don't promise the ability."
---

# Intelligence center

![Intelligence center store card](../assets/bases/com-center_card.png)

Extends the signal radius around the base.

## In game

**The purchase card.** This is what a player sees before buying.

![Intelligence center purchase card](../assets/bases/com-center_buy.png)

Below the description it shows: Nothing at all.

There is no row because its `zoneProperty` is null, so there is nothing to draw.

**The module once built.** This is the panel the player opens at the base.

![Intelligence center in use](../assets/bases/com-center_owned.png)

If your module does not produce a panel like this one, it is not configured correctly. The numbers here and the numbers on the purchase card are the same values, read from the same place.

!!! note "Documented for custom modules"
    Saber's own documentation lists this module's zoneProperty and says these props exist to configure CUSTOM FOB modules.
    Use the property named below, not one you inferred from a symbol name.

## Identity

| | |
|---|---|
| `zoneProperty.moduleId` | `ANTENNA` |
| Zone property | `null` |
| Its members | moduleId |

## Models

| Slot | Model |
|---|---|
| `modelId` (main base) | `models_fob_module_com_center` |
| `modelIdAdditional` (outpost) | `models_fob_module_small_com_center` |
| `modelAnimated` | `models_fob_module_com_center_objective` |
| `modelAdditionalAnimated` | `models_fob_module_small_com_center_objective` |

## Artwork: every image slot

Six images appear per module, in six different places. They are
separate images, not one picture reused.

| Where you see it | Field | Falls back to | Symbol for this module |
|---|---|---|---|
| Store sidebar, the list row | `bg` | `moduleSlotContent` | `moduleComCenter` |
| Store card, when you select it | `popupModuleBg` | (none) | `moduleComCenterPopup` |
| Right card, when the module is used | `bgRight` | `moduleSlotContentRight` | `moduleComCenterRight` |
| HUD strip of deployed modules | `bgSmall` | `moduleSlotContentSmall` | `moduleComCenterSmall` |
| **On the map** | `iconMap40` | (none) | `(none ships)` |
| Trade panel glyph | `iconTrade` | (none) | `(none ships)` |

!!! warning "How much of that is confirmed"
    The **fallbacks** are the engine schema defaults, so they are fact.
    The **symbols** in the last column are confirmed to exist in the
    game's UI bundle. Which field each one is wired to is **inferred
    from its suffix** and has not been verified against a module proven
    to work. Treat the last column as a strong lead, not as settled.

### Replacing them

!!! note "There is a template for this"
    [expeditions-module-art-template.zip](../assets/downloads/expeditions-module-art-template.zip) — the four
    canvases at the right sizes, named correctly, with the cropped and
    covered areas marked.

The four background images may be your own PNGs. Ship them at
`ui/textures/<name>.png` and name them in the descriptor **without the
folder and without `.png`**. These are the sizes mods on disk ship:

```
ui/textures/mymodule_bg.png       ->  "bg": "mymodule_bg"             380 x 92
ui/textures/mymodule_popup.png    ->  "popupModuleBg": "..."          380 x 92
ui/textures/mymodule_right.png    ->  "bgRight": "..."                760 x 90
ui/textures/mymodule_small.png    ->  "bgSmall": "..."                124 x 52
```

⛔ The two icons may not be your own files. `iconMap40` and `iconTrade`
take a symbol from the game's bundle; a PNG in an icon field does not
render. Borrow a vanilla symbol instead.

!!! note "The other five image fields"
    `icon20`, `icon40`, `iconModuleBg`, `tradeArrowsSpecialIcon` and
    `uiDescTradeHeaderIcon` are unset on every module examined, and take
    symbols only.

!!! warning "popupModuleBg is not validated, and has failed in practice"
    The module checker tests `bg`, `bgSmall` and `bgRight` but not this
    field, and a shipped mod has shown a broken-image placeholder here —
    a yellow square with a red mountain. If you see that, the name did
    not resolve.

### The four background images, rebuilt

Where each one is drawn, on the real screens:

![Intelligence center slot placement](../assets/bases/com-center_placement.png)

The originals live inside the game's UI bundle and cannot be
extracted, so these are rebuilt from in-game captures. **Every one
below is a transparent PNG at the slot aspect — the same thing you
have to author.** The game supplies the brown row, the slate card and
the tan bar; your file supplies only the model.

!!! warning "These are FOUR separate images, not one image reused"
    Do not render your model once and drop the same picture into all
    four fields. Across the vanilla set the four differ in **crop,
    framing and left-to-right orientation**.

    **Three of the twelve are flipped in the store row**: Expanded
    parking, Cargo drone and Service station. The other nine run the
    same way in both slots.

    Those three have one thing in common. The feature that identifies
    the module sits on the LEFT of the purchase card — the parking
    barrier and cabinet, the drone itself, the hoist gantry — and the
    store row clips its left edge. Flipping is what saves that detail
    from the crop.

    **So the rule is: flip when the detail that identifies your module
    would otherwise be cropped away.** Decide it per slot by looking at
    what survives, not by reusing one render four times.

The slot sizes below are measured, not quoted: 762 x 184, 762 x 184,
1530 x 184 and 248 x 104 in a 2160p frame, which is exactly the
documented 380 x 92, 380 x 92, 760 x 90 and 124 x 52 doubled.

!!! note "Why bg shows the whole model when the game clips it"
    In game the store row cuts off the left of this art. That is the
    game drawing it, not your file — you author the complete model and
    let the row clip. The example below is the complete image.

`bg` — 380 x 92 — the store row **and** the sell dialog. Fills the row height and **clips off the left edge**.

![Intelligence center bg](../assets/bases/com-center_bg.png)

This store-row art runs the **same way** as the purchase card.

`popupModuleBg` — 380 x 92 — the purchase card. The **whole model**, nothing cropped.

![Intelligence center popup](../assets/bases/com-center_popup.png)

`bgRight` — 760 x 90 — the banner above the module card when it is in use. The artwork is **aligned to the RIGHT**; the icon and name sit on the tan bar to its left.

![Intelligence center bgRight](../assets/bases/com-center_right.png)

`bgSmall` — 124 x 52 — the HUD strip of deployed modules. A **tight, centred crop** that fills the chip, cropped on every side — not the same fit as `bg`.

![Intelligence center bgSmall](../assets/bases/com-center_small.png)

!!! note "Composition"
    Vanilla rows are **left-anchored**, fill the row height, and clip
    off the left edge. A centred picture with margins reads as too
    small and floats. Match the framing, not just the pixel size.

## Building your own: the ability does not work

!!! danger "A custom antenna module never reveals anything"
    You can make one, and the player can build it, see it, sell it and get
    the refund. Its ability, marking nearby air drops as question marks on the
    map, never fires. Tested in game on a vanilla map, where nothing starts
    revealed. Saber ended support in September 2026, so this won't be patched.

Everything else about the module works. Measured with Gimbo's Resource
Scanner, an `AntennaUpgradeDesc` mod:

| | Result |
|---|---|
| Appears in the Base modules panel | works |
| Builds, and its model stands at the base | works |
| Saved and reloaded under its own name | works |
| Sells, and the refund arrives | works |
| **Marks air drops in range** | **never** |

**Why, as far as it's known.** The game's script decides whether a built
module is an antenna by comparing the descriptor's name with the word
`ANTENNA`. A mod's descriptor carries its own name, so the comparison
always fails. `zoneProperty.moduleId` isn't read at that point, which is why
no descriptor setting reaches it.

**What was tried, and failed.** The game's compiled script was patched so
those checks answered to the mod's name instead. The patched script loaded
(a marker in it showed up in the running game), and the module still revealed
nothing on the Carpathians. Its range was then cut from 6,000 to 600, the
stock antenna's value, and it still revealed nothing. Why the patch failed
is not known. Don't spend time on the range; it isn't the cause.

!!! note "Correction: `zoneProperty` is not null for a mod"
    Earlier versions of this page said to use `null` here, because Saber's
    documentation does. Measured: a mod antenna with a `null` zoneProperty
    registered in none of five saves. `ZonePropertyFobModuleDefault` with
    `moduleId: "ANTENNA"` registers and deploys. The `null` is right for
    Saber's own antenna and wrong for yours.

### What to do instead

- **Don't promise the ability.** If your module's text says it finds air
  drops, players will report it as broken, and they'll be right.
- **Give it a job that works for a mod.** Storage, fuel and repair modules
  built on `ZonePropertyFobModuleStorage` do work. See
  [What the module does](../60-custom/base-modules-reference.html#what-the-module-does-zoneproperty).
- **Or make it about money,** as Gimbo's Resource Scanner now is: `cost`
  1,000 and `sellPrice` 500,000, with a description that owns the joke. A
  sold custom module leaves its model standing on the map (true of every
  module with a custom model), but the cash arrives every time.

Whatever you build, give it a `moduleId` **no other mod uses**. Your own mod
name works.

See [Every base module, and every surface you can edit](../60-custom/base-modules-reference.html) for the full field list.
