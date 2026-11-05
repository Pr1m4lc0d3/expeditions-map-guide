---
title: Gateways between maps
part: Zones
order: 460
summary: How to link two custom maps so a truck drives from one to the other, which Saber's guide says is not supported.
status: draft
---

A gateway is a zone that sends the player's truck to a zone on another map. It is
how vanilla joins a surface map to its cave.

Saber's guide says custom regions of several linked maps are not supported in
Expeditions, and that both maps of a gateway must be in the same region.
<span class="prov prov-doc">documented</span> **Gateways work anyway, and you don't
need a region.** Two ordinary standalone maps have been linked and driven between
on PC, with a stock truck and a custom one.
<span class="prov prov-unver">tested in game</span>

!!! warning "This page is a draft"
    This rests on one pair of small test maps. The list at the end says what has
    not been tested.

## What you need

- Two maps, each packed to a `.pak`, each with a deploy zone.
- A gateway zone on each map, each pointing at the other.

Both maps must be installed. The player starts on one of them like any other custom
map.

## Step 1: give each map four built-in ground layers

Do this first, because getting it wrong crashes the game the moment a truck
arrives, and the error says nothing useful.

A map's material needs its layers filled in, and **the base layer must be a
built-in tile**, not a custom one. Saber's guide says a new material has four
layers, and every working map checked has four in its source file.
<span class="prov prov-doc">documented</span>

A custom tile can be left out of the compiled map without warning. A map whose only
layer was a custom tile compiled with **zero** ground layers. The game asks what
surface a truck is standing on, finds an empty list, and crashes.
<span class="prov prov-unver">measured</span> In the editor that map drew black and
could not be painted, so **black ground is your warning sign.**

## Step 2: place the gateway zones

Place a zone on each map and give it a `ZonePropertyGateway` prop. The tested zones
were round, 30 m across. Keep the target zone clear of models and plants with
collision, because trucks arrive inside it. <span class="prov prov-doc">documented</span>

| Field | What to set |
|---|---|
| `levelZoneLink` | the target, see step 3 |
| `cameraDir` | any non-zero direction, such as `1, 0, 0`. All zeros gives a black screen <span class="prov prov-doc">documented</span> |
| `cameraPos` | where the arrival camera starts |
| `animationTime` | length of the arrival camera move in milliseconds. The test used 3000 |
| `isShown`, `isAffectedByZoneSettings` | `true` |

Both zones need the prop. Saber warns that a gateway whose partner has no
`ZonePropertyGateway` crashes during the transfer.
<span class="prov prov-doc">documented</span>

## Step 3: write the link with the real level name

This is the step that made the crossing work. Once a map is installed, the game
calls it `mod_level_<name>`, not `level_<name>`. The link has to use that name:

```
mod_level_gate_two || gate_two
```

The part before `||` is the level. The part after is the zone on that level.

**Packing rewrites this line.** The packed map's `zone_settings.json` comes out as
`level_gate_two || gate_two`, a level that doesn't exist. Each pack needs the link
corrected inside the `.pak` afterward. <span class="prov prov-unver">tested in game</span>

Two wrong forms, and what they do:

| Link | Result |
|---|---|
| `level_gate_two \|\| gate_two` | names a level that doesn't exist |
| `` ~#@%$`*level_gate_two~#@%$`* \|\| gate_two `` | the prompt shows the raw text, and pressing Let's go drops you to the main menu <span class="prov prov-unver">tested in game</span> |

That second form is what Saber's hidden region tool writes. The game only swaps it
for the real name when it loads a region's files, not in a map's own `.pak`.
<span class="prov prov-unver">measured</span>

## What the player sees

Drive into the zone and a **Travel to** prompt appears. Press it, and a popup offers
**Let's go** and **Not now**. The truck then arrives in the target zone, and the
gateway on that side brings it back.

![A truck inside a gateway zone on the first test map, with the Travel to Gate Two prompt at the bottom of the screen](../assets/gateways/travel-prompt-gate-one.jpg)

![The same truck after crossing, on the second test map, whose ground is painted green, with a Travel to Gate One prompt](../assets/gateways/arrived-gate-two.jpg)

The popup needs two images, `Size_800x520` and `Size_800x520_Gray`, in `uiImages`.
<span class="prov prov-doc">documented</span> Without them it shows an empty picture
and logs an error, but the crossing still works.
<span class="prov prov-unver">tested in game</span>

## Not yet known

- Whether a `mod_level_` link can be kept through a pack, so that no correction is
  needed afterward.
- How to deliver a linked set of maps to other players, and whether a map installed
  through mod.io still goes by `mod_level_<name>`.
- Whether a mission can span both maps. Without a region, each map keeps its own
  expedition, and the crossing was tested in free roam only.
- Whether a cave works. Vanilla caves use `caveSettings`, with `isCave` and
  `surfaceMapID`, and `isCave` on the gateway. None of that has been tried on a
  custom map.
- More than two maps, or more than one gateway on a map.
- Popup images, locked gateways, and anything carried across.
- Any platform other than PC.
