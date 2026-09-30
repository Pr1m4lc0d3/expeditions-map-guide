---
title: Roads are not carved terrain
part: The land
order: 230
status: outline
summary: Roads are Overlay objects laid on top of the ground, and two of the defaults are backwards for a usable road.
---

This is the biggest single time sink for a new map maker: sculpting roads into the
heightmap by hand when the editor has a road tool.

Planned for this page:

- roads are **Overlay** objects, not terrain modifications
- overlay nodes are 2D. There is no height on a node
- the defaults are wrong for a drivable road. Flatten defaults to off, so the road does
  not level the ground under it, and the offset defaults to on, which deliberately adds
  ruts
- how an overlay interacts with the terrain underneath it
- when you want to sculpt as well as overlay
