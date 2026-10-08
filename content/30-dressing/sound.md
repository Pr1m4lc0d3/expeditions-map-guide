---
title: Music and sound
part: Dressing the map
order: 340
summary: Background music is a table keyed by level name and can be added to a map that is already packed. Ambient sound cannot. How to tell which one you are holding, and the two pak members that decide whether anyone but you hears it.
---

# Music and sound

Music and ambient sound look like one feature and behave like two. Music is a
lookup table the game reads at runtime. Ambient sound is part of the scene.

That difference decides how much work a change costs, so it is worth being able
to tell them apart before you start.

## The test

`pak.load_list` inside a packed map is the engine's index of that level's
resources. Count what appears in it. On a shipped map that plays four music
tracks and has an ambient eagle call:

```
references to 'eagle'            28
references to 'magic_whispers'    0
references to 'music_presets'     0
```

The ambient sound is indexed. The music is not.

| | in the index | in the scene | needs the editor |
|---|---|---|---|
| music | no | no | **no** |
| ambient or positional sound | yes | yes | yes |

So **music can be added to a map that is already finished and packed.** An
ambient sound has a position, which means opening the map, placing it, saving,
repacking, and getting it into the index.

## The table

`Media/classes/sounds/music_presets.xml`, one block per level:

```xml
<LevelMusic LevelName="level_my_map">
  <Sound Name="music/track_a" StartTime="24"   EndTime="6"    FadeInTime="30" FadeOutTime="10" />
  <Sound Name="music/track_b" StartTime="6"    EndTime="13"   FadeInTime="30" FadeOutTime="10" />
  <Sound Name="music/track_c" StartTime="13"   EndTime="20.5" FadeInTime="30" FadeOutTime="10" />
  <Sound Name="music/track_d" StartTime="20.5" EndTime="24"   FadeInTime="30" FadeOutTime="10" />
</LevelMusic>
```

- `LevelName` is the level folder name, spelled exactly, including case.
- `Name` is `music/<slug>` with no extension.
- Each `Sound` owns a window of the in-game 24 hour clock. Midnight is written
  `24`, as both a start and an end.

**The windows have to tile the whole day.** An hour no window covers is silence
at that hour. If you only have one track, give it two windows, `24` to `12` and
`12` to `24`, rather than one window from `24` to `24`, which is not documented
and may mean the whole day or none of it.

A track shorter than a game day already loops inside its own window, so an extra
restart at a boundary costs nothing you can hear.

## Where the audio actually ships

This is the part that catches people, because a map can sound finished in your
own game and ship silent.

```
Media/sounds/music/<slug>.wav             your copy, for local play
<map>.pak        member  classes/sounds\music_presets.xml
<map>_pc.pak     member  sounds/music\<slug>.wav
```

Your `Media` folder is a development artifact. Somebody who installs your mod has
the pak files and nothing else, so **the audio has to be inside a pak or they
hear nothing.**

The main pak carries the table and no audio at all. The audio lives in the
per-platform pak, in that platform's codec: `.wav` for `_pc`, `.mp3` for the
PlayStation variants, `.xma` for the Xbox variants.

## Format

Every music track the game ships is 16-bit stereo PCM. Sample rate is not
strict: shipped tracks include both 44.1 kHz and 48 kHz and both play. Length is
not strict either, and the shipped ones run from 81 to 182 seconds.

Length costs download size rather than compatibility, because the pak member is
uncompressed audio. At 48 kHz stereo 16-bit that is roughly 11 MB per minute
before the archive compresses it.

## Silencing music in one place

`<NoMusicSoundDomain>` polygons in the level's `_sounds.xml` mute music inside an
area. That is the intended way to make one location quiet, rather than removing
the level's music and losing it everywhere.

## After a repack

A repack rebuilds the pak from scratch, so both members go away while the table
still says the level has music. The symptom is silence with nothing else wrong,
and nothing reports it.

If you script your packing, re-inject after every pack. The agent toolkit does
this with `install_music.py <level> --reapply`.

## Two things that will delist your map

Both come from editing a pak directly, and both fail with no error at all.

**Member names are not all spelled the same way,** and the inconsistency is in
the shipped files. Names under `[...]` use backslashes throughout, names under
`ui/` use forward slashes throughout, and everything else uses a forward slash
first and backslashes after it. Copy the working spelling; do not tidy it.

**Python's `zipfile` rewrites backslashes to forward slashes when it reads an
archive.** On an untouched shipped map, 19 of 31 member names come back altered.
Rebuild the pak from those names and the game can no longer find those members.
The map then vanishes from the level list with no error, no log line and no crash
dump.

Level paks are also padded to a multiple of 4096 bytes. One that ends flush is
not listed.
