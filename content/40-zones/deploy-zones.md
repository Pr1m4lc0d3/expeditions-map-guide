---
title: Deploy zones and FOBs
part: Zones
order: 420
status: outline
summary: Where trucks arrive, and how a base with a store, a workshop and a fuel pump is actually assembled.
---

A deploy zone is the one zone type every map must have. Building a base around it is
more involved than it looks, because each module is a **pair** of zones.

Planned for this page:

- the deploy property, the default deploy point, and the truck limit
- the default deploy point also selects which FOB model is used, medium or small
- sit deploy zones slightly **above** the terrain to avoid collision problems
- the base module needs a storage property on the deploy zone itself, flagged as being
  at the deploy zone and as always spawning, plus a link back to the deploy zone
- the store needs its own link, also back to the deploy zone
- **every buildable FOB module is two zones.** A placement zone, which carries no
  properties at all and defines where the model goes, and an interaction zone, which
  carries a base-building property linking to the placement zone
- placement zone dimensions: 10 x 10 m for a main base, 7 x 7 m for a secondary outpost
- the full list of module ids
