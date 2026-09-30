---
title: Where everything lives
part: Start here
order: 120
summary: Your map exists in three places at once and they drift apart. This is the single most common source of wasted days, so it comes before anything else.
---

Your map is not one thing in one folder. It exists in **three** places, they hold
different data, and they fall out of step with each other constantly.

Almost every "I fixed it and nothing changed" story ends here. So does almost
every "it worked yesterday". Learn this page and you will skip a category of
problem entirely.

## The three copies

All three live under `Documents\My Games\Expeditions\Media\`.

| Folder | What it is | Who writes it | Who reads it |
|---|---|---|---|
| `prebuild\<level>\` | **The source.** Your real work lives here | The editor, when you save | The editor, when you open the map |
| `levels\<Level>\` | **The staging copy.** What the zone settings tool shows you, and what the packer reads | The editor and the zone tool | The packer |
| `Mods\<Level>.pak` | **The product.** A zip archive | The packer | **The game** |

Read that last column again. **The game only ever reads the `.pak`.** Nothing you
do in `prebuild` or `levels` changes what you see when you press Deploy until you
pack again.

!!! warning "The mistake everyone makes once"
    You find a bad value, you fix it in the `.pak` because that is the file the
    game reads, and it works. Then you pack the map again and your fix is gone,
    because the pack was built from the source, which you never touched.

    **Fix the source. Then pack.** Editing the pak is for emergencies, not for
    work you want to keep.

## The flow, in one direction

```
     you, in the editor
             │  save
             ▼
   prebuild\<level>\          ← the source. edit here.
             │  the editor copies forward
             ▼
   levels\<Level>\            ← staging. the zone tool reads this.
             │  Pack (about 25 minutes)
             ▼
   Mods\<Level>.pak           ← the game reads only this.
```

It flows one way. There is no "sync back".

## Closing the editor is a write, not a stop

This one costs people a whole evening.

While the editor has your map open, it holds the entire map in memory. When you
close it, **it writes that memory back over your files.** So if you edit
`prebuild` by hand while the editor is open, closing the editor silently throws
your edit away.

The safe order is always:

<div class="step"><div class="n">1</div><div>

In the editor: **save**, then **close it**.

</div></div>
<div class="step"><div class="n">2</div><div>

Make your file edits now, with the editor shut.

</div></div>
<div class="step"><div class="n">3</div><div>

Open the editor again. It reads your edits.

</div></div>
<div class="step"><div class="n">4</div><div>

Pack.

</div></div>

## Packing rewrites some of your work

The pack step is not a simple copy. It rebuilds parts of your map from what the
editor has in memory, and one of the things it rebuilds is the list of zones.

**Zone properties can be discarded during a pack.** The zone names survive,
because they come from the objects placed in your scene, but the settings you
attached to those names can be regenerated as an empty list. If you pack and your
deploy zone stops working, this is the first thing to check, not the last.

The habit that protects you: after every pack, open the packed file and confirm
your zones still have properties. It takes seconds and it catches a failure that
otherwise costs you a whole test cycle.

## Zone names: spaces in the source, underscores in the pack

A genuinely nasty one, and it is worth understanding now rather than discovering
it three weeks in.

- The **editor** matches a zone's settings to the object in your scene by name,
  and scene names contain **spaces**. Rename them with underscores in the source
  and the editor stops finding them, so your settings silently detach.
- The **game** splits one of its internal zone references on **whitespace**. A
  zone whose name contains a space can never be looted and can never receive
  delivered items.

No single spelling satisfies both. So:

!!! tip "The rule"
    **Spaces in the source. Underscores in the pack.**

    Keep your source names as the editor made them, with spaces. After packing,
    convert the names of any zone that holds or receives items to underscores.
    Every time you pack.

This affects storage zones, airdrops and construction zones. It does not affect a
zone that is only a deploy point, because nothing passes through it.

## Cloning a map

Copying a finished map to start a new one is a good habit with one trap in it.

A map's identity is a token stored in `user_name_of_map.txt`, and a copy still
holds the **original's** name. Two maps then claim to be the same map, and the
game loads whichever it finds first.

The symptom is bewildering and worth memorising, because you will never guess the
cause from it: *"this is an older version of the map I just packed."*

If you clone a map, change the identity in every file that carries it, or do not
clone at all.

## What to take away

- edit `prebuild`, never the pak
- close the editor **before** hand-editing, because closing it overwrites
- the game only sees the pak, so nothing counts until you pack
- check your zone properties survived the pack
- convert item-carrying zone names to underscores after packing
- a cloned map needs its own identity
