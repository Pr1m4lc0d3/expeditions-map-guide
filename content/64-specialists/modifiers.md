---
title: Every ability
part: Appendix B - specialists
order: 948
summary: "All 47 specialist modifier types: what each does, every field with its type and default, and the shipped specialists that carry it."
---

# Every ability

The engine defines **47 modifier types**. In a descriptor each is
written as `SpecialistModifier` plus the name below. Field names must be copied
exactly, misspellings included (`Consumpion`, `Suspencion`, `Inceased`,
`Guaranted`); a correctly spelled field is ignored.

Each type also has a label field for every value (the field name plus
`UiDesc`). Those control the text on the card, and any ability may also carry
`overrideUiDesc` to replace its card line with your own text. Both are covered under
[When an ability never appears on the card](../60-custom/specialists.html#when-an-ability-works-but-never-appears-on-the-card).

Types and defaults are from the editor's type definitions. "Shipped values"
lists every vanilla specialist that carries the ability.

## AdditionalAddonSupplies

More fuel, parts, wheels in consumable addons

| Field | Type | Default |
|---|---|---|
| `additionalAddonFuelCount` | int | 0 |
| `additionalAddonRepairsCount` | int | 0 |
| `additionalAddonWheelsCount` | int | 0 |

**Shipped values:** Angela Mayer (`additionalAddonFuelCount` 10); Justin Goodman (`additionalAddonRepairsCount` 20)

## AdditionalDeployResources

More fuel, parts, wheels at every open deploy zone

| Field | Type | Default |
|---|---|---|
| `additionalDeployFuelCount` | int | 0 |
| `additionalDeployRepairsCount` | int | 0 |
| `additionalDeployWheelsCount` | int | 0 |

**Shipped values:** Connor Eriksen (`additionalDeployFuelCount` 100, `additionalDeployRepairsCount` 200)

## AdditionalReward

Bigger money rewards

| Field | Type | Default |
|---|---|---|
| `additionalRewardExpeditionIncreasedPercent` | int | 0 |
| `additionalRewardSideQuestsIncreasedPercent` | int | 0 |
| `additionalRewardTasksIncreasedPercent` | int | 0 |

**Shipped values:** Henry McOir (`additionalRewardExpeditionIncreasedPercent` 20, `additionalRewardSideQuestsIncreasedPercent` 20, `additionalRewardTasksIncreasedPercent` 30)

## AdditionalTreasureItems

Extra treasure items in resource zones

| Field | Type | Default |
|---|---|---|
| `additionalTreasureItemsCount` | int | 0 |
| `additionalItem` | mod | — |

**Shipped values:** Henry McOir (`additionalTreasureItemsCount` 1)

## AirdropReroll

Pay to reroll an airdrop

| Field | Type | Default |
|---|---|---|
| `airdropRerollCost` | int | 0 |
| `airdropRerollLootLists` | LootList | — |

**Shipped values:** Philip de Fichent (`airdropRerollCost` 2000)

## AnchorRadius

Bigger anchor placement radius

| Field | Type | Default |
|---|---|---|
| `anchorIDs` | string | — |
| `anchorRadiusIncreasedPercent` | int | 0 |

**Shipped values:** Mike Nixon (`anchorRadiusIncreasedPercent` 100)

## AnchorSupplies

More anchor charges

| Field | Type | Default |
|---|---|---|
| `anchorIDs` | string | — |
| `anchorMaxLimitCount` | int | 0 |

**Shipped values:** Mike Nixon (`anchorMaxLimitCount` 5)

## ArmorCapacity

Raises the armor cap on four truck parts

| Field | Type | Default |
|---|---|---|
| `armorEngineIncreasedPercent` | int | 0 |
| `armorGearboxIncreasedPercent` | int | 0 |
| `armorGasTankIncreasedPercent` | int | 0 |
| `armorSuspencionIncreasedPercent` | int | 0 |

**Shipped values:** Dmytro Koval (`armorEngineIncreasedPercent` 30, `armorGearboxIncreasedPercent` 30, `armorGasTankIncreasedPercent` 30, `armorSuspencionIncreasedPercent` 30)

## ArmorRestoreEverywhere

Add armor anywhere (no fields)

No fields: carrying the modifier is the ability.

**Shipped values:** Dmytro Koval (no fields)

## BinocularRadius

Bigger binocular reveal

| Field | Type | Default |
|---|---|---|
| `binocularPartRadiusIncreasedMeters` | int | 0 |
| `binocularFullRadiusIncreasedMeters` | int | 0 |

**Shipped values:** Connor Eriksen (`binocularPartRadiusIncreasedMeters` 150); Angela Mayer (`binocularPartRadiusIncreasedMeters` 100); Justin Goodman (`binocularPartRadiusIncreasedMeters` 100); Eric Miller (`binocularFullRadiusIncreasedMeters` 100)

## DroneAcceleration

Faster air drone

| Field | Type | Default |
|---|---|---|
| `droneAccelerationIncreasedPercent` | int | 0 |
| `droneAccelerationHeightIncreasedPercent` | int | 0 |

**Shipped values:** Akane Ishida (`droneAccelerationIncreasedPercent` 30, `droneAccelerationHeightIncreasedPercent` 30); Lance Silva (`droneAccelerationIncreasedPercent` 30, `droneAccelerationHeightIncreasedPercent` 30); Naval Desayi (`droneAccelerationIncreasedPercent` 70, `droneAccelerationHeightIncreasedPercent` 70)

## DroneControllability

Air drone handling

| Field | Type | Default |
|---|---|---|
| `droneControllabilityResForceIncreasedPercent` | int | 0 |
| `droneControllabilityResForceRotationIncreasedPercent` | int | 0 |
| `droneControllabilityForceRotationIncreasedPercent` | int | 0 |

**Shipped values:** Akane Ishida (`droneControllabilityResForceIncreasedPercent` 20, `droneControllabilityResForceRotationIncreasedPercent` 20, `droneControllabilityForceRotationIncreasedPercent` 20); Lance Silva (`droneControllabilityResForceIncreasedPercent` 20, `droneControllabilityResForceRotationIncreasedPercent` 20, `droneControllabilityForceRotationIncreasedPercent` 20); Naval Desayi (`droneControllabilityResForceIncreasedPercent` 30, `droneControllabilityResForceRotationIncreasedPercent` 30, `droneControllabilityForceRotationIncreasedPercent` 30); Alicia Silverwood (`droneControllabilityResForceIncreasedPercent` 50, `droneControllabilityResForceRotationIncreasedPercent` 50, `droneControllabilityForceRotationIncreasedPercent` 50)

## DroneDiscoverScoutZones

No fields. **No vanilla specialist uses it; never observed.**

No fields: carrying the modifier is the ability.

**Shipped values:** no shipped specialist carries it.

## DroneHeight

Higher air drone ceiling

| Field | Type | Default |
|---|---|---|
| `droneHeightIncreasedMeters` | int | 0 |

**Shipped values:** Akane Ishida (`droneHeightIncreasedMeters` 20)

## DroneItemSetup

Air drone item placement

| Field | Type | Default |
|---|---|---|
| `droneItemSetupSettings` | mod | — |

**Shipped values:** Alicia Silverwood (no fields)

## DroneMaxSpeed

Higher air drone top speed

| Field | Type | Default |
|---|---|---|
| `droneMaxSpeedIncreasedPercent` | int | 0 |

**Shipped values:** Naval Desayi (`droneMaxSpeedIncreasedPercent` 70); Alicia Silverwood (`droneMaxSpeedIncreasedPercent` 25); Alicia Silverwood (`droneMaxSpeedIncreasedPercent` 25)

## DroneRadius

Longer air drone range

| Field | Type | Default |
|---|---|---|
| `droneRadiusIncreasedMeters` | int | 0 |

**Shipped values:** Akane Ishida (`droneRadiusIncreasedMeters` 200); Lance Silva (`droneRadiusIncreasedMeters` 50); Naval Desayi (`droneRadiusIncreasedMeters` 50)

## DroneScoutRadius

Bigger air drone reveal

| Field | Type | Default |
|---|---|---|
| `droneFullScoutRadiusIncreasedMeters` | int | 0 |
| `dronePartScoutRadiusIncreasedMeters` | int | 0 |

**Shipped values:** Akane Ishida (`droneFullScoutRadiusIncreasedMeters` 0, `dronePartScoutRadiusIncreasedMeters` 50); Naval Desayi (`droneFullScoutRadiusIncreasedMeters` 50)

## DroneTrade

Trade by air drone (no fields)

No fields: carrying the modifier is the ability.

**Shipped values:** Lance Silva (no fields)

## EcholotModeAura

Echo sounder becomes an aura around the truck

| Field | Type | Default |
|---|---|---|
| `echolotRadiusOverrideMeters` | int | 0 |
| `echolotStepCountOverride` | int | 0 |
| `echolotApplicationAdditionalTime` | float | 0 |

**Shipped values:** Bruce Brown (no fields)

## EcholotModeCone

Echo sounder becomes a cone ahead

| Field | Type | Default |
|---|---|---|
| `echolotRadiusOverrideMeters` | int | 0 |
| `echolotStepCountOverride` | int | 0 |
| `echolotConeAngle` | float | 360 |
| `echolotApplicationAdditionalTime` | float | 0 |

**Shipped values:** Dayaana Tumusova (`echolotConeAngle` 45, `echolotApplicationAdditionalTime` 1)

## EcholotModeSnow

Echo sounder measures snow

| Field | Type | Default |
|---|---|---|
| `echolotRadiusOverrideMeters` | int | 0 |
| `echolotStepCountOverride` | int | 0 |

**Shipped values:** Benjamin Anchor (`echolotRadiusOverrideMeters` 20, `echolotStepCountOverride` 20)

## ElectricityConsumption

Less charge used

| Field | Type | Default |
|---|---|---|
| `wheelDroneElectricityConsumptionReducedPercent` | int | 0 |
| `wheelDroneAbilityElectricityConsumptionReducedPercent` | int | 0 |
| `metaldetectorElectricityConsumptionReducedPercent` | int | 0 |
| `radarElectricityConsumptionReducedPercent` | int | 0 |

**Shipped values:** Thomas Stevenson (`wheelDroneElectricityConsumptionReducedPercent` 30, `wheelDroneAbilityElectricityConsumptionReducedPercent` 30, `metaldetectorElectricityConsumptionReducedPercent` 30, `radarElectricityConsumptionReducedPercent` 30)

## EmergencyStockSupplies

Bigger emergency stock in the truck

| Field | Type | Default |
|---|---|---|
| `emergencyStockFuel` | int | 0 |
| `emergencyStockRepairs` | int | 0 |
| `emergencyStockWheels` | int | 0 |

**Shipped values:** Justin Goodman (`emergencyStockRepairs` 50, `emergencyStockWheels` 2)

## EmergencyWinch

Winch with the engine off but not broken

| Field | Type | Default |
|---|---|---|
| `winchFuelPerMinute` | float | 1 |

**Shipped values:** Marcus Kingsley (`winchFuelPerMinute` 20)

## EngineUnderwaterDamage

Less engine damage underwater

| Field | Type | Default |
|---|---|---|
| `engineUnderwaterDamageReducedPercent` | int | 0 |

**Shipped values:** Anwar Farsi (`engineUnderwaterDamageReducedPercent` 100); Dayaana Tumusova (`engineUnderwaterDamageReducedPercent` 50)

## FogOfWarTranspRadius

Bigger reveal around the truck

| Field | Type | Default |
|---|---|---|
| `fogOfWarRadiusInceasedMeters` | int | 0 |
| `fogOfWarTranspRadiusInceasedMeters` | int | 0 |

**Shipped values:** Brian Wilson (`fogOfWarTranspRadiusInceasedMeters` 10); Mitch Goodman (`fogOfWarTranspRadiusInceasedMeters` 10); Solveig Friedenlund (`fogOfWarTranspRadiusInceasedMeters` 20)

## FreeEvacuation

Free evacuations

| Field | Type | Default |
|---|---|---|
| `freeEvacuationMaxLimitCount` | int | 0 |

**Shipped values:** Zarema Abdurafieva (`freeEvacuationMaxLimitCount` 1)

## FuelConsumption

Less fuel used

| Field | Type | Default |
|---|---|---|
| `fuelConsumpionReducedPercent` | int | 0 |

**Shipped values:** Michelle Redrock (`fuelConsumpionReducedPercent` 15); Dmytro Koval (`fuelConsumpionReducedPercent` 20)

## GuaranteedAirdropResource

Airdrops always hold some resources

| Field | Type | Default |
|---|---|---|
| `guarantedAirdropFuelCount` | int | 0 |
| `guarantedAirdropRepairCount` | int | 0 |
| `guarantedAirdropWheelCount` | int | 0 |

**Shipped values:** Angela Mayer (`guarantedAirdropFuelCount` 50)

## ImproveWinchedTruck

A driverless truck being winched gets stronger

| Field | Type | Default |
|---|---|---|
| `engineResponsivenessIncreasedPercent` | int | 0 |
| `torqueIncreasedPercent` | int | 0 |
| `onModelFrictionIncreasedPercent` | int | 0 |
| `bodyFrictionAsphaltIncreasedPercent` | int | 0 |
| `substanceFrictionIncreasedPercent` | int | 0 |
| `bodyFrictionIncreasedPercent` | int | 0 |
| `fuelConsumptionReducedPercent` | int | 0 |

**Shipped values:** Solveig Friedenlund (`engineResponsivenessIncreasedPercent` 30, `torqueIncreasedPercent` 30, `onModelFrictionIncreasedPercent` 30, `bodyFrictionAsphaltIncreasedPercent` 30, `substanceFrictionIncreasedPercent` 30, `bodyFrictionIncreasedPercent` 30, `fuelConsumptionReducedPercent` 30)

## ItemCost

Cheaper items

| Field | Type | Default |
|---|---|---|
| `itemCostReducedPercent` | int | 0 |

**Shipped values:** Zarema Abdurafieva (`itemCostReducedPercent` 10)

## ItemSellPrice

Items sell for more

| Field | Type | Default |
|---|---|---|
| `itemSellPriceIncreasedPercent` | int | 0 |

**Shipped values:** Zarema Abdurafieva (`itemSellPriceIncreasedPercent` 30); Philip de Fichent (`itemSellPriceIncreasedPercent` 30)

## JackscrewSupplies

More jack screw charges

| Field | Type | Default |
|---|---|---|
| `jackscrewMaxLimitCount` | int | 0 |

**Shipped values:** Brian Wilson (`jackscrewMaxLimitCount` 2)

## MayDiscoverZones

Can identify zones flagged for this class

| Field | Type | Default |
|---|---|---|
| `mayDiscoverZonesByBinocular` | bool | False |
| `mayDiscoverZonesByDrone` | bool | False |

**Shipped values:** Connor Eriksen (no fields); Angela Mayer (no fields); Justin Goodman (no fields); Park Won-shin (no fields); Anwar Farsi (no fields); Bruce Brown (no fields); Dayaana Tumusova (no fields); Benjamin Anchor (no fields); Brian Wilson (no fields); Eric Miller (no fields); Mitch Goodman (no fields); Solveig Friedenlund (no fields); Akane Ishida (no fields); Lance Silva (no fields); Naval Desayi (no fields); Alicia Silverwood (no fields)

## RepairBuildingConsumption

Fewer parts to repair bridges and clear debris

| Field | Type | Default |
|---|---|---|
| `repairBuildingConsumptionReducedPercent` | float | 20 |
| `repairBuildingConsumptionDesc` | mod | — |

**Shipped values:** Marcus Kingsley (`repairBuildingConsumptionReducedPercent` 40)

## RepairConsumption

Fewer parts per repair

| Field | Type | Default |
|---|---|---|
| `repairConsumpionReducedPercent` | int | 0 |

**Shipped values:** Michelle Redrock (`repairConsumpionReducedPercent` 30)

## TreasureItemSellPrice

Treasure sells for more

| Field | Type | Default |
|---|---|---|
| `treasureItemSellPriceIncreasedPercent` | int | 0 |

**Shipped values:** David Simmons (`treasureItemSellPriceIncreasedPercent` 50)

## TruckDamage

Less damage to truck parts

| Field | Type | Default |
|---|---|---|
| `truckDamageEngineReducedPercent` | int | 0 |
| `truckDamageGearboxReducedPercent` | int | 0 |
| `truckDamageGasTankReducedPercent` | int | 0 |
| `truckDamageSuspensionReducedPercent` | int | 0 |
| `truckDamageWheelReducedPercent` | int | 0 |

**Shipped values:** Mike Nixon (`truckDamageEngineReducedPercent` 30, `truckDamageGearboxReducedPercent` 30, `truckDamageGasTankReducedPercent` 30, `truckDamageSuspensionReducedPercent` 30); Michelle Redrock (`truckDamageEngineReducedPercent` 15, `truckDamageGearboxReducedPercent` 15, `truckDamageGasTankReducedPercent` 15, `truckDamageSuspensionReducedPercent` 15); Marcus Kingsley (`truckDamageEngineReducedPercent` 10, `truckDamageGearboxReducedPercent` 10, `truckDamageGasTankReducedPercent` 10, `truckDamageSuspensionReducedPercent` 10, `truckDamageWheelReducedPercent` 10); Eric Miller (`truckDamageWheelReducedPercent` 50)

## UnderwaterAnchorSetup

Place anchors underwater (no fields)

No fields: carrying the modifier is the ability.

**Shipped values:** Bruce Brown (no fields)

## WheelDroneArmor

Armor on the ground drone

| Field | Type | Default |
|---|---|---|
| `wheelDroneArmorEngineIncreasedPercent` | int | 0 |
| `wheelDroneArmorBatteryIncreasedPercent` | int | 0 |
| `wheelDroneArmorSuspencionIncreasedPercent` | int | 0 |

**Shipped values:** Thomas Stevenson (`wheelDroneArmorEngineIncreasedPercent` 30, `wheelDroneArmorBatteryIncreasedPercent` 30, `wheelDroneArmorSuspencionIncreasedPercent` 30)

## WheelDroneArmorRestoreEverywhere

Repair ground drone armor anywhere (no fields)

No fields: carrying the modifier is the ability.

**Shipped values:** Thomas Stevenson (no fields)

## WheelDroneFriction

Ground drone grip

| Field | Type | Default |
|---|---|---|
| `wheelDroneOnModelFrictionIncreasedPercent` | int | 0 |
| `wheelDroneBodyFrictionAsphaltIncreasedPercent` | int | 0 |
| `wheelDroneSubstanceFrictionIncreasedPercent` | int | 0 |
| `wheelDroneBodyFrictionIncreasedPercent` | int | 0 |

**Shipped values:** Park Won-shin (`wheelDroneOnModelFrictionIncreasedPercent` 200, `wheelDroneBodyFrictionAsphaltIncreasedPercent` 200, `wheelDroneSubstanceFrictionIncreasedPercent` 200, `wheelDroneBodyFrictionIncreasedPercent` 200)

## WheelDroneScoutRadius

Ground drone reveal

| Field | Type | Default |
|---|---|---|
| `wheelDroneFullScoutRadiusIncreasedMeters` | int | 0 |
| `wheelDronePartScoutRadiusIncreasedMeters` | int | 0 |

**Shipped values:** Park Won-shin (`wheelDroneFullScoutRadiusIncreasedMeters` 100, `wheelDronePartScoutRadiusIncreasedMeters` 100)

## WheelDroneTorque

Ground drone torque

| Field | Type | Default |
|---|---|---|
| `wheelDroneTorqueIncreasedPercent` | int | 0 |

**Shipped values:** Thomas Stevenson (`wheelDroneTorqueIncreasedPercent` 50)

## WheelDroneZone

Bigger signal zones on the map

| Field | Type | Default |
|---|---|---|
| `wheelDroneZoneIncreasedPercent` | int | 0 |

**Shipped values:** Park Won-shin (`wheelDroneZoneIncreasedPercent` 50)

## WinchImprove

Longer, stronger winch

| Field | Type | Default |
|---|---|---|
| `winchLengthIncreasedMeters` | int | 0 |
| `winchPowerIncreasedPercent` | int | 0 |

**Shipped values:** Mitch Goodman (`winchLengthIncreasedMeters` 10, `winchPowerIncreasedPercent` 30)

