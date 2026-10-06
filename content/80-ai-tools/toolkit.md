---
title: The toolkit
part: AI tools
order: 830
summary: The scripts that read and write map and vehicle files directly. Plain Python, runnable by hand, no AI required.
---

# The toolkit

`F:\Expeditions\Toolkit` is a folder of Python scripts that read and write the
game's files directly. An agent uses them, but there is nothing AI about them —
run them yourself from a terminal.

They exist for the work the editor structurally cannot do: operations whose
target changes continuously along a path, and operations over a whole network at
once. **Do not reimplement the editor's brushes.** Use the editor for sculpting
and placement; use these for the rest.

## Read the documentation first

The single highest-value command here:

```
python wiki.py howto <road|river|trees|terrain|zones|sounds|overlays>
```

It returns every page for that topic from the 514-page official mirror, in
reading order. `howto road` returns nine pages about overlays.

This exists because a day was lost carving roads into a heightmap while the
editor's actual road tool sat indexed in that wiki the whole time.

```
python wiki.py search "<phrase>"      # full-text across the docs
python wiki.py schema <type>          # the editor's own type definitions
```

!!! note "Test a search tool with a question, not a keyword"
    The index returned nothing useful for "how do I make a road" for months,
    because it was only ever tested with words that were already known to be in
    it.

## Terrain and roads

| need | command |
|---|---|
| real-world elevation | `fetch_terrain.py <lat> <lon> --span --blocks` |
| lay a road network | `make_overlays.py <level>` |
| cut a graded bench | `sculpt_roads.py` |
| smooth a roadway | `smooth_roadway.py` |
| push heights into tiles | `push_heights.py` |
| clear scatter from a road | `clear_roadway.py`, `sync_tiles.py` |
| rivers | `paint_river.py`, `shape_river.py` |
| build a whole map from real terrain | `build_map.py` |

!!! warning "A push into tiles is a merge, never a copy"
    Tiles hold hand sculpting done after the master was written. Protect water
    channels and take explicit no-go areas for ground you reshaped by hand.

Cap terrain movement near 3 m. Forcing a gradient onto a bad alignment once
produced 30 m embankments, and a surface 30 m different from its surroundings has
a cliff at every boundary.

## Models

| need | command |
|---|---|
| what models exist | `stock_models.py`, `list_installed_models.py` |
| re-seat placements | `reseat_models.py` |
| move a group | `move_cluster.py` |
| check a custom model converts and loads | `verify_model.py` |

`verify_model.py` exists because `ResourceConverter --mod-convert -s` only tells
you the files parse. Twenty-nine models passed it and then crashed the editor on
placement. The script converts, keeps the output, and inspects the artifact the
engine actually reads.

!!! warning "Scale is meaningless without the mesh"
    Read the bounding box out of the mesh and specify sizes in metres. Copying a
    scale distribution across a different mix of brands once turned a 6.84 m
    boulder into a 227 m potato stuck to a cliff.

## Missions and zones

| need | command |
|---|---|
| validate objectives before packing | `check_objectives.py <level>` / `--pak` / `--all` |
| author the gameplay layer | `build_missions.py` |

Run `check_objectives.py` before every pack. Objective errors are silent: a stage
where every substage is optional is prohibited and errors, a null
`localOffsetScoutingAreaRelativeZone` crashes, and a dangling `globalZoneId`
hangs Deploy with no popup and no log line.

## Packing and checking

| need | command |
|---|---|
| pack a map | `pack_map.py` |
| patch one member in place | `patch_member.py` |
| identify a pak | `pak_fingerprint.py` |
| a map misbehaves | `check_pack.py <Level>` |

**`check_pack.py` comes before any theory.** When a map misbehaves, run it first
and read what it says, rather than reasoning about what might be wrong.

!!! danger "`apply_loot_naming.py` is disabled"
    It is still in the folder, and its own header says so: it broke a map for a
    week and must not be run. Older notes that tell you to run it after every
    pack are out of date.

## Custom content

| need | command |
|---|---|
| validate a FOB module | `check_fob_module.py` |
| pack a FOB module | `pack_fob_module.py` |

An invalid `$type` in a FOB module is **silently nulled at pack time**, which is
why a validator exists.

## Vehicles

```
python port_vehicle.py analyze <mod.zip>
python port_vehicle.py port <mod.zip> --id <modid> --name "My Truck"
```

Brings a SnowRunner vehicle into Expeditions: works out the required textures,
writes source `.tga` maps, encodes them with the game's own converter, rebuilds
`pc.pak`, installs and registers the mod.

| flag | effect |
|---|---|
| `--donor <dir>` | reuse real `.tga` files where the names match. Defaults to the game's own sample mod, so genuine template textures are preferred over invented ones |
| `--palette <json>` | `{"material": [r,g,b]}` colour overrides |
| `--no-install` | build only, do not touch your mod folder |
| `--work <dir>` | scratch directory |
| `--skip-self-test` | skip the encoder verification. Do not |

It verifies the encoder against a file the game itself produced before it changes
anything, and refuses to continue if that check fails. The full explanation is in
[Porting a SnowRunner truck](../65-vehicles/porting-a-truck.html).

## Conventions these scripts follow

**Measure, then claim.** Report the number, not the impression.

**A zero result is a claim.** Run a positive control before citing one. A search
that returns nothing may be a search that was not looking in the right place.

**Never write a backup into a folder the editor scans.** Backups left in
`subgroups\` were loaded as empty SubGroups, and the symptom was models that
would not highlight and snap appearing broken — both selection-driven, so one
bug wearing two faces.
