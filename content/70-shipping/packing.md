---
title: Packing your map
part: Shipping
order: 710
summary: What packing actually does, why it takes 25 minutes, and what it changes behind your back.
---

# Packing your map

The game never reads your source files. It reads **paks**: the archives in
`Documents\My Games\Expeditions\Media\Mods\`. Packing is the step that turns the
map you edit into the files the game loads, and the same is true of a custom
module, specialist or item.

The flow runs one way. You edit the source, you pack, the game reads the pak.
Nothing in the pak flows back into your source, so a fix made only in the pak is
lost the next time you pack.

## What the pack produces

### A map

Pack a map with the editor's **Pack terrain** button. Saber's documentation
describes two sets of output:

- **`.pak` files**, for playing the map yourself. They are copied into
  `Media\Mods\` automatically.
- **`.zip` files**, for uploading to mod.io. They go to `Media\levels\`.

There are several files because the game runs on several platforms. A packed
map on disk looks like this:

```
Media\Mods\
    level_<Map>.pak                    the map itself
    level_<Map>_pc.pak                 one pak per platform
    level_<Map>_nx64.pak
    level_<Map>_playstation_4.pak
    level_<Map>_playstation_5.pak
    level_<Map>_xbox_one.pak
    level_<Map>_xbox_series.pak
Media\levels\
    level_<Map>_pc.zip                 one zip per platform, for mod.io
    level_<Map>_nx64.zip               ... and four more
```

Each platform zip holds the main map pak and that platform's pak. The main pak
holds the map's settings as readable JSON (`zone_settings.json`,
`objective_settings.json`, `level_desc.json` and others), the compiled scene in
`[scene]/`, the terrain textures, and any store art.

**Restart the game after packing.** It looks for new paks only at launch. A map
needs at least one Expedition and one Deploy zone to load; see
[A map that loads](../00-start/map-that-loads.html).

### A custom module, specialist or item

These are packed from the **EXP MODs creation** dialog with **File > Pack**,
not with Pack terrain. The paks go to the root of `Media\Mods\`. For a base
module, Saber's documentation puts the zips in the module's own folder there.

For a base module the toolkit's `pack_fob_module.py` does the same job without
the editor, and avoids its traps (below). It writes
`BaseUpgradeDesc_<name>.pak` and a `BaseUpgradeDesc_<name>_pc.pak` carrying the
textures. The whole module process is on
[Custom FOB modules](../60-custom/fob-modules.html).

## Why it takes around 25 minutes

Packing a map takes about 25 minutes on the maps built for this guide. It
writes output for six platforms, not one. **A long pack is not a hang.** Let it
finish.

The 25 minutes is what shapes the way you should work. Every test in the game
costs a pack, so a trial-and-error loop costs half an hour per attempt. Catch
mistakes before you pack: `check_objectives.py` checks the objective layer in a
second, against the source.

```
python check_objectives.py <level>
```

Saber's own validator writes `base\logs\ModMapError.txt` at pack time, which is
too late to save the pack, and on this project it has been empty every time it
was read.

## What the pack rewrites behind your back

This is the part that matters. The pack is not a plain copy, and several things
come out different from what you put in. None of them announces itself.

### Zone properties can come back empty

The editor's pack has twice written a skeleton `zone_settings.json`, silently
dropping **every zone property on the map**: loot, deploy, recovery and the
bridge construction zones. Zone names survive, because they come from the
objects in your scene, but the settings attached to them are gone. The file is
still valid JSON and the map still loads. Why it happens is not known.

The fix is to restore the properties in the **source** and pack again. See
[My zone settings vanished](troubleshooting.html#my-zone-settings-vanished).

### Zone names are baked in and cannot be changed afterwards

A packed map holds each zone's name twice: in the editable
`zone_settings.json`, and in `[scene]/data_for_ssl.bin`, which is compiled at
pack time and cannot be edited. The two must match exactly.

Rename zones in a packed map and the names no longer match the compiled scene.
If one of them is a deploy zone, the Deploy screen builds empty and the game
hangs, with no popup, no log line and no crash dump. Fix zone names in the
source, before packing.

This collides with a second rule. The editor matches settings to your scene by
name, and scene names may contain spaces; the game splits item references on
spaces, so a zone that holds items cannot have one. See
[Loot and deliveries do nothing](troubleshooting.html#loot-and-deliveries-do-nothing).

### An invalid type is emptied, not rejected

A descriptor with an invalid `$type` is silently nulled at pack time. The source
looks right and the pak holds nothing. If a fix seems to have no
effect, compare the packed file with the source before anything else.

### A module pack can swallow its own output

The editor packs a module from its folder, and it writes its platform zips into
that same folder. The next pack sweeps those zips into the new pak, and the zips
built around it grow again. One measured pack took a module pak from 2.4 MB to
73 MB. Nothing errors and the module keeps working.

**Delete the platform zips from the module folder before every pack.** The pack
rebuilds them, so nothing is lost. `check_fob_module.py` reports zips in the
folder as a warning and zips inside the pak as an error.
`pack_fob_module.py` packs only what belongs in the pak, so it cannot do this.

## The check to run every single time

Before you spend half an hour testing in the game, spend a second checking the
pack:

```
python check_pack.py <Level>
python check_objectives.py <Level> --pak
```

`check_pack.py` compares the packed map with your source and reports, on one
screen:

- how many zones have properties in the source and in the pak, and says plainly
  if the pack dropped any
- construction zones that existed in the source and are missing from the pak
- zone names missing from the compiled scene, deploy zones first
- zone references that point at nothing, which is what hangs the Deploy screen
- free-roam stages with an empty map field, which makes the game load a
  different map

It ends with `OK - the pack preserved everything` or `NOT OK - see above`. If the
pack dropped the zone properties, `--restore-source` copies a known-good
snapshot of the zone files back over the source so you can pack again; the
snapshot folder is set in the script.

For a module, run `check_fob_module.py` on the folder or the pak. To check only
the bytes of any pak against the rules below:

```
python expeditions_oracle.py pak <file.pak>
```

!!! warning "A clean check is not a working map"
    These checks catch the failures that are known. The game is the test.

## Changing a packed file

The right fix is in the source, followed by a fresh pack. A change made only in
the pak works for one test and disappears at the next pack.

When a single test justifies it, change one member in place with
`patch_member.py` or `pak_splice.py`. Both copy the original pak byte for byte
and replace only the member you name.

!!! danger "Never write a pak while the game is running"
    A running game keeps using the pak it already opened. The write appears to
    succeed, the session plays on with the old content, and whatever you
    conclude gets credited to the wrong version. `pak_splice.py` refuses to run
    while the game is open.

## Rules for any tool that writes a pak

A pak is an ordinary ZIP archive, but the game is stricter about it than any
zip tool:

| Rule | What breaks |
|---|---|
| Map paks are **STORED** (uncompressed); mod paks are **DEFLATE** | rebuilding a map pak produces one the game will not list |
| No **extra field** in any entry's local header | the game drops that entry; a 36-byte NTFS timestamp block is enough |
| Do not re-encode a map pak; splice the changed member | a rebuilt map pak is refused even when it looks identical |

The extra-field trap catches Python's `zipfile` in particular: copying an
entry's `extra` writes it into the local header as well as the directory, and
`zipfile` only ever shows you the directory. `pack_fob_module.py` builds every
entry fresh and walks the local headers to check.

The editor pads paks with zeros to a multiple of 4096 bytes. For a mod pak that
padding does not matter: the mod paks confirmed working in game are plain
unpadded zips.

## Distributing a finished map

Upload the zips from `Media\levels\` to mod.io. Saber's instructions: upload
**each platform's zip as a separate file**, and tick that file's platform on the
same page. A wrong platform tick produces no error.

!!! danger "Never rebuild the distribution zip with a general-purpose zip tool"
    Upload the zips exactly as the pack wrote them. A map distribution zip that
    was rebuilt once stopped the map listing in the game. The zip's byte layout
    matters, not only its contents: no extra fields in either header, and the
    compression of each member as the editor wrote it.

To change a published map, change the source and pack again. That produces a
fresh, matching set of paks and zips.
