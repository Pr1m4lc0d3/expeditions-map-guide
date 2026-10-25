---
title: Every base module
part: Appendix A - base modules
order: 899
summary: The twelve modules that ship with the game, one page each, with their screenshots, models and every image slot.
---

# Every base module

One page for each of the twelve modules that ship with the game. The first thing on each page is whether a custom module of that kind works in game, and the table below gives all twelve at once. Each page
shows the module in game, its identity, its models, and all of its artwork
slots, so you can copy what works when you build your own.

To build a module of your own, start with
[Custom FOB modules](../60-custom/fob-modules.html). Every descriptor field is listed in the
[Module descriptor reference](../60-custom/base-modules-reference.html).

| Module | As a custom module | What it does |
|---|---|---|
| [Gas station](gas-station.html) | **✅ Works** | Sells fuel to a truck parked at the zone. |
| [Warehouse](extra-storage.html) | **✅ Works** | Holds cargo at the base. |
| [Essentials storage](double-stock.html) | **✅ Works** | Holds some fuel, wheels and spare parts, resupplied between deployments. |
| [Workshop](workshop.html) | **✅ Works** | Crafts items from spare parts; refills only by recycling items. |
| [Repair station](repair-station.html) | **✅ Works** | Stocks spare parts and wheels for trucks to take. |
| [Service station](service-station.html) | **✅ Works** | Lets trucks in its area spend spare parts on armor, up to +20%. |
| [Generator](generator.html) | **⛔ Broken** | Converts fuel into electricity. |
| [Helipad](helicopter.html) | **✅ Works** | Transports the player between discovered zones. |
| [Expanded parking](parking.html) | **⚠ Not yet tested** | Raises how many trucks the deploy zone holds. |
| [Cargo drone](drone-base.html) | **✅ Works** | Recovers ground drones at the deploy zone. |
| [Intelligence center](com-center.html) | **⛔ Broken** | Marks nearby air drops on the map. |
| [Tow truck](evacuator.html) | **⚠ Not yet tested** | Recovers a stranded truck back to the base. |

Every verdict comes from a test recorded in the toolkit's logs. "Not yet tested" means nobody has checked in game that a custom one does its job, so nothing is claimed either way.

!!! warning "True of every custom module that uses its own model"
    Selling it frees the slot and pays the refund, but the model stays standing on the map. This can't be fixed.
