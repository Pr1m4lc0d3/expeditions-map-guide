---
title: Every specialist
part: Appendix B - specialists
order: 940
summary: "The six specialist classes and all 25 shipped specialists, with their costs and abilities, read from the game's own data."
---

# Every specialist

The game ships **25 specialists** in **six classes**. This appendix lists them
all, with the exact values the game uses, so you can copy what works and beat
it on purpose. To make your own, start with
[Custom specialists](../60-custom/specialists.html).

- [Descriptor settings](descriptor.html): every field of a specialist file.
- [Every ability](modifiers.html): all 47 modifier types, their fields,
  and which shipped specialists carry them.

Every number here was read from the game: the specialists from
`initial.cache_block` inside `preload/paks/client/initial.pak`, the names and
class descriptions from the game's English strings, and the fields from the
editor's type definitions.

## The six classes

The class is the tab a specialist is listed under. The saved file stores the
number in the first column. It decides nothing else: any class can carry any
ability.

| `speciality` | Class | Schema name | Shipped | The game's description |
|---|---|---|---|---|
| `0` | [Mechanic](mechanic.html) | `MECHANIC` | 5 | Mechanics keep the trucks running throughout the expeditions and improve the effectiveness of anchors |
| `1` | [Logistician](logistician.html) | `LOGISTICS_SPECIALIST` | 4 | Logistics reduce the cost of deploy and allow you to use binoculars more efficiently |
| `2` | [Hydrologist](hydrologist.html) | `HYDROLOGIST` | 4 | Hydrologists open access to special equipment and help the engine run longer underwater |
| `3` | [Jaeger](jaeger.html) | `JAEGER` | 4 | Jaegers are real experts in survival in extreme conditions; they find paths and pave new ones |
| `4` | [Operator](operator.html) | `OPERATOR` | 4 | Operators open access to the drone and help to use it more efficiently |
| `5` | [Manager](manager.html) | `MANAGER` | 4 | Managers help to earn more money for completing expeditions, can increase the amount of prepayment |

`6` is `NONE`. Saber documents that it crashes the game. Never use it.

!!! note "Spelling"
    Saber's guide writes `LOGISTIC_SPECIALIST`. The editor schema and the
    game's own data say `LOGISTICS_SPECIALIST`; the game calls the class
    Logistician on screen.

## All 25 shipped specialists

| Name | Class | Cost | Abilities |
|---|---|---|---|
| Mike Nixon | [Mechanic](mechanic.html) | 600 | [`AnchorSupplies`](modifiers.html#anchorsupplies), [`AnchorRadius`](modifiers.html#anchorradius), [`TruckDamage`](modifiers.html#truckdamage) |
| Dmytro Koval | [Mechanic](mechanic.html) | 800 | [`ArmorCapacity`](modifiers.html#armorcapacity), [`ArmorRestoreEverywhere`](modifiers.html#armorrestoreeverywhere), [`FuelConsumption`](modifiers.html#fuelconsumption) |
| Thomas Stevenson | [Mechanic](mechanic.html) | 1,200 | [`ElectricityConsumption`](modifiers.html#electricityconsumption), [`WheelDroneTorque`](modifiers.html#wheeldronetorque), [`WheelDroneArmor`](modifiers.html#wheeldronearmor), [`WheelDroneArmorRestoreEverywhere`](modifiers.html#wheeldronearmorrestoreeverywhere) |
| Michelle Redrock | [Mechanic](mechanic.html) | 1,400 | [`RepairConsumption`](modifiers.html#repairconsumption), [`TruckDamage`](modifiers.html#truckdamage), [`FuelConsumption`](modifiers.html#fuelconsumption) |
| Marcus Kingsley | [Mechanic](mechanic.html) | 1,500 | [`EmergencyWinch`](modifiers.html#emergencywinch), [`RepairBuildingConsumption`](modifiers.html#repairbuildingconsumption), [`TruckDamage`](modifiers.html#truckdamage) |
| Connor Eriksen | [Logistician](logistician.html) | 500 | [`AdditionalDeployResources`](modifiers.html#additionaldeployresources), [`BinocularRadius`](modifiers.html#binocularradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Angela Mayer | [Logistician](logistician.html) | 900 | [`GuaranteedAirdropResource`](modifiers.html#guaranteedairdropresource), [`AdditionalAddonSupplies`](modifiers.html#additionaladdonsupplies), [`BinocularRadius`](modifiers.html#binocularradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Justin Goodman | [Logistician](logistician.html) | 1,000 | [`EmergencyStockSupplies`](modifiers.html#emergencystocksupplies), [`AdditionalAddonSupplies`](modifiers.html#additionaladdonsupplies), [`BinocularRadius`](modifiers.html#binocularradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Park Won-shin | [Logistician](logistician.html) | 1,000 | [`WheelDroneZone`](modifiers.html#wheeldronezone), [`WheelDroneFriction`](modifiers.html#wheeldronefriction), [`WheelDroneScoutRadius`](modifiers.html#wheeldronescoutradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Anwar Farsi | [Hydrologist](hydrologist.html) | 600 | [`EngineUnderwaterDamage`](modifiers.html#engineunderwaterdamage), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Dayaana Tumusova | [Hydrologist](hydrologist.html) | 1,000 | [`EcholotModeCone`](modifiers.html#echolotmodecone), [`EngineUnderwaterDamage`](modifiers.html#engineunderwaterdamage), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Benjamin Anchor | [Hydrologist](hydrologist.html) | 1,200 | [`EcholotModeSnow`](modifiers.html#echolotmodesnow), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Bruce Brown | [Hydrologist](hydrologist.html) | 1,500 | [`EcholotModeAura`](modifiers.html#echolotmodeaura), [`UnderwaterAnchorSetup`](modifiers.html#underwateranchorsetup), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Brian Wilson | [Jaeger](jaeger.html) | 700 | [`JackscrewSupplies`](modifiers.html#jackscrewsupplies), [`FogOfWarTranspRadius`](modifiers.html#fogofwartranspradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Eric Miller | [Jaeger](jaeger.html) | 900 | [`TruckDamage`](modifiers.html#truckdamage), [`BinocularRadius`](modifiers.html#binocularradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Solveig Friedenlund | [Jaeger](jaeger.html) | 1,100 | [`ImproveWinchedTruck`](modifiers.html#improvewinchedtruck), [`FogOfWarTranspRadius`](modifiers.html#fogofwartranspradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Mitch Goodman | [Jaeger](jaeger.html) | 1,300 | [`WinchImprove`](modifiers.html#winchimprove), [`FogOfWarTranspRadius`](modifiers.html#fogofwartranspradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Akane Ishida | [Operator](operator.html) | 600 | [`DroneRadius`](modifiers.html#droneradius), [`DroneHeight`](modifiers.html#droneheight), [`DroneScoutRadius`](modifiers.html#dronescoutradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones), [`DroneAcceleration`](modifiers.html#droneacceleration), [`DroneControllability`](modifiers.html#dronecontrollability) |
| Lance Silva | [Operator](operator.html) | 900 | [`DroneTrade`](modifiers.html#dronetrade), [`DroneRadius`](modifiers.html#droneradius), [`MayDiscoverZones`](modifiers.html#maydiscoverzones), [`DroneAcceleration`](modifiers.html#droneacceleration), [`DroneControllability`](modifiers.html#dronecontrollability) |
| Naval Desayi | [Operator](operator.html) | 1,200 | [`DroneMaxSpeed`](modifiers.html#dronemaxspeed), [`DroneScoutRadius`](modifiers.html#dronescoutradius), [`DroneRadius`](modifiers.html#droneradius), [`DroneControllability`](modifiers.html#dronecontrollability), [`DroneAcceleration`](modifiers.html#droneacceleration), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| Alicia Silverwood | [Operator](operator.html) | 1,200 | [`DroneItemSetup`](modifiers.html#droneitemsetup), [`DroneMaxSpeed`](modifiers.html#dronemaxspeed), [`DroneMaxSpeed`](modifiers.html#dronemaxspeed), [`DroneControllability`](modifiers.html#dronecontrollability), [`MayDiscoverZones`](modifiers.html#maydiscoverzones) |
| David Simmons | [Manager](manager.html) | 700 | [`TreasureItemSellPrice`](modifiers.html#treasureitemsellprice) |
| Zarema Abdurafieva | [Manager](manager.html) | 1,500 | [`FreeEvacuation`](modifiers.html#freeevacuation), [`ItemCost`](modifiers.html#itemcost), [`ItemSellPrice`](modifiers.html#itemsellprice) |
| Philip de Fichent | [Manager](manager.html) | 2,000 | [`AirdropReroll`](modifiers.html#airdropreroll), [`ItemSellPrice`](modifiers.html#itemsellprice) |
| Henry McOir | [Manager](manager.html) | 3,000 | [`AdditionalReward`](modifiers.html#additionalreward), [`AdditionalTreasureItems`](modifiers.html#additionaltreasureitems) |

Every shipped specialist except one starts locked and is unlocked through play.
A custom specialist should leave `isLocked` false; see
[Locking](../60-custom/specialists.html#locking).
