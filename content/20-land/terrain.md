---
title: How terrain actually works
part: The land
order: 210
status: outline
summary: Heightmaps, the tile system, and why editing the file you think is the terrain often changes nothing.
---

The editor does not build terrain from the large master images you might expect. It
builds it from **tiles**, one per chunk of the map, and it reads them **when the map
is opened** rather than when you press Rebuild Terrain.

Planned for this page:

- the tile layout, and why the full-texture folder and the height source are not what
  the game actually uses
- the height source is a quarter of the master's linear resolution
- height is stored at 16-bit float precision, so the smallest possible step is roughly
  the elevation divided by 2048. About 10 cm at 200 m up, about 2 cm in a valley
- why that floor cannot be filtered away, and why **flattening a road makes the
  stepping more visible** rather than less
- the practical consequence: route roads low on the map
- pushing edited heights back into tiles is a **merge**, not a copy, because the tiles
  hold hand sculpting done after the master was written
