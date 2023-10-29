from ..Resource.Oil import CrudeOil
from ..Resource.Ore import Ore, Bauxite, CateriumOre, Coal, CopperOre, IronOre, Limestone, RawQuartz, Sulfur, Uranium
from ..Resource.Resource import *


class Machine:
    recipes = {
        'Example Recipe': {
            'consumption': {
                IronOre: 1
            },
            'production': {
                IronIngot: 1
            }
        }
    }
    def __init__(self, recipe_name, clock_speed_modifier=1):
        if clock_speed_modifier > 2.5 or clock_speed_modifier < .25:
            raise ValueError('Invalid clock speed percentage!')

        self.consumption_rates = {resource: round(rate * clock_speed_modifier, 4) for resource, rate in self.recipes[recipe_name]["consumption"].items()}
        self.production_rates = {resource: round(rate * clock_speed_modifier, 4) for resource, rate in self.recipes[recipe_name]["production"].items()}

        self.allow_undersupply = False

    def get_consumption_rates(self):
        return self.consumption_rates

    def get_production_rates(self):
        return self.production_rates

    def get_allow_undersupply(self):
        return self.allow_undersupply


class Assembler(Machine):
    recipes = {
        'Adhered Iron Plate': {
            'consumption': {
                IronPlate: 11.25,
                Rubber: 3.75
            },
            'production': {
                ReinforcedIronPlate: 3.8
            }
        },
        'AI Limiter': {
            'consumption': {
                CopperSheet: 25,
                Quickwire: 100
            },
            'production': {
                AILimiter: 5
            }
        },
        'Alclad Aluminum Sheet': {
            'consumption': {
                AluminumIngot: 30,
                CopperSheet: 10
            },
            'production': {
                AlcladAluminumSheet: 30
            }
        },
        'Alclad Casing': {
            'consumption': {
                AluminumIngot: 150,
                CopperIngot: 75
            },
            'production': {
                AluminumCasing: 112.5
            }
        },
        'Assembly Director System': {
            'consumption': {
                AdaptiveControlUnit: 1.5,
                Supercomputer: 0.75
            },
            'production': {
                AssemblyDirectorSystem: 0.8
            }
        },
        'Automated Wiring': {
            'consumption': {
                Stator: 2.5,
                Cable: 50
            },
            'production': {
                AutomatedWiring: 2.5
            }
        },
        'Black Powder': {
            'consumption': {
                Coal: 15,
                Sulfur: 15
            },
            'production': {
                BlackPowder: 30
            }
        },
        'Bolted Frame': {
            'consumption': {
                ReinforcedIronPlate: 7.5,
                Screw: 140
            },
            'production': {
                ModularFrame: 5
            }
        },
        'Bolted Iron Plate': {
            'consumption': {
                IronPlate: 90,
                Screw: 250
            },
            'production': {
                ReinforcedIronPlate: 15
            }
        },
        'Caterium Circuit Board': {
            'consumption': {
                Plastic: 12.5,
                Quickwire: 37.5
            },
            'production': {
                CircuitBoard: 8.8
            }
        },
        'Cheap Silica': {
            'consumption': {
                RawQuartz: 11.25,
                Limestone: 18.75
            },
            'production': {
                Silica: 26.3
            }
        },
        'Circuit Board': {
            'consumption': {
                CopperSheet: 15,
                Plastic: 30
            },
            'production': {
                CircuitBoard: 7.5
            }
        },
        'Cluster Nobelisk': {
            'consumption': {
                Nobelisk: 7.5,
                SmokelessPowder: 10
            },
            'production': {
                ClusterNobelisk: 2.5
            }
        },
        'Coated Iron Canister': {
            'consumption': {
                IronPlate: 30,
                CopperSheet: 15
            },
            'production': {
                EmptyCanister: 60
            }
        },
        'Coated Iron Plate': {
            'consumption': {
                IronIngot: 50,
                Plastic: 10
            },
            'production': {
                IronPlate: 75
            }
        },
        'Compacted Coal': {
            'consumption': {
                Coal: 25,
                Sulfur: 25
            },
            'production': {
                CompactedCoal: 25
            }
        },
        'Copper Rotor': {
            'consumption': {
                CopperSheet: 22.5,
                Screw: 195
            },
            'production': {
                Rotor: 11.3
            }
        },
        'Crystal Computer': {
            'consumption': {
                CircuitBoard: 7.5,
                CrystalOscillator: 2.8125
            },
            'production': {
                Computer: 2.8
            }
        },
        'Electric Motor': {
            'consumption': {
                ElectromagneticControlRod: 3.75,
                Rotor: 7.5
            },
            'production': {
                Motor: 7.5
            }
        },
        'Electrode Circuit Board': {
            'consumption': {
                Rubber: 30,
                PetroleumCoke: 45
            },
            'production': {
                CircuitBoard: 5
            }
        },
        'Electromagnetic Connection Rod': {
            'consumption': {
                Stator: 8,
                HighSpeedConnector: 4
            },
            'production': {
                ElectromagneticControlRod: 8
            }
        },
        'Electromagnetic Control Rod': {
            'consumption': {
                Stator: 6,
                AILimiter: 4
            },
            'production': {
                ElectromagneticControlRod: 4
            }
        },
        'Encased Industrial Beam': {
            'consumption': {
                SteelBeam: 24,
                Concrete: 30
            },
            'production': {
                EncasedIndustrialBeam: 6
            }
        },
        'Encased Industrial Pipe': {
            'consumption': {
                SteelPipe: 28,
                Concrete: 20
            },
            'production': {
                EncasedIndustrialBeam: 4
            }
        },
        'Encased Plutonium Cell': {
            'consumption': {
                PlutoniumPellet: 10,
                Concrete: 20
            },
            'production': {
                EncasedPlutoniumCell: 5
            }
        },
        'Fabric': {
            'consumption': {
                Mycelia: 15,
                Biomass: 75
            },
            'production': {
                Fabric: 15
            }
        },
        'Fine Black Powder': {
            'consumption': {
                Sulfur: 7.5,
                CompactedCoal: 3.75
            },
            'production': {
                BlackPowder: 15
            }
        },
        'Fine Concrete': {
            'consumption': {
                Silica: 7.5,
                Limestone: 30
            },
            'production': {
                Concrete: 25
            }
        },
        'Fused Quickwire': {
            'consumption': {
                CateriumIngot: 7.5,
                CopperIngot: 37.5
            },
            'production': {
                Quickwire: 90
            }
        },
        'Fused Wire': {
            'consumption': {
                CopperIngot: 12,
                CateriumIngot: 3
            },
            'production': {
                Wire: 90
            }
        },
        'Gas Nobelisk': {
            'consumption': {
                Nobelisk: 5,
                Biomass: 50
            },
            'production': {
                GasNobelisk: 5
            }
        },
        'Heat Exchanger': {
            'consumption': {
                AluminumCasing: 30,
                Rubber: 30
            },
            'production': {
                HeatSink: 10
            }
        },
        'Heat Sink': {
            'consumption': {
                AlcladAluminumSheet: 37.5,
                CopperSheet: 22.5
            },
            'production': {
                HeatSink: 7.5
            }
        },
        'Homing Riffle Ammo': {
            'consumption': {
                RifleAmmo: 50,
                HighSpeedConnector: 2.5
            },
            'production': {
                HomingRifleAmmo: 25
            }
        },
        'Insulated Cable': {
            'consumption': {
                Wire: 45,
                Rubber: 30
            },
            'production': {
                Cable: 100
            }
        },
        'Modular Frame': {
            'consumption': {
                ReinforcedIronPlate: 3,
                IronRod: 12
            },
            'production': {
                ModularFrame: 2
            }
        },
        'Motor': {
            'consumption': {
                Rotor: 10,
                Stator: 10
            },
            'production': {
                Motor: 5
            }
        },
        'Nobelisk': {
            'consumption': {
                SteelPipe: 20,
                BlackPowder: 20
            },
            'production': {
                Nobelisk: 10
            }
        },
        'OC Supercomputer': {
            'consumption': {
                RadioControlUnit: 9,
                CoolingSystem: 9
            },
            'production': {
                Supercomputer: 3
            }
        },
        'Plutonium Fuel Unit': {
            'consumption': {
                EncasedPlutoniumCell: 10,
                PressureConversionCube: 0.5
            },
            'production': {
                PlutoniumFuelRod: 0.5
            }
        },
        'Pressure Conversion Cube': {
            'consumption': {
                FusedModularFrame: 1,
                RadioControlUnit: 2
            },
            'production': {
                PressureConversionCube: 1
            }
        },
        'Pulse Nobelisk': {
            'consumption': {
                Nobelisk: 5,
                CrystalOscillator: 1
            },
            'production': {
                PulseNobelisk: 5
            }
        },
        'Quickwire Cable': {
            'consumption': {
                Quickwire: 7.5,
                Rubber: 5
            },
            'production': {
                Cable: 27.5
            }
        },
        'Quickwire Stator': {
            'consumption': {
                SteelPipe: 16,
                Quickwire: 60
            },
            'production': {
                Stator: 2
            }
        },
        'Reinforced Iron Plate': {
            'consumption': {
                IronPlate: 30,
                Screw: 60
            },
            'production': {
                ReinforcedIronPlate: 5
            }
        },
        'Rifle Ammo': {
            'consumption': {
                CopperSheet: 15,
                SmokelessPowder: 10
            },
            'production': {
                RifleAmmo: 75
            }
        },
        'Rotor': {
            'consumption': {
                IronRod: 20,
                Screw: 100
            },
            'production': {
                Rotor: 4
            }
        },
        'Rubber Concrete': {
            'consumption': {
                Limestone: 50,
                Rubber: 10
            },
            'production': {
                Concrete: 45
            }
        },
        'Shatter Rebar': {
            'consumption': {
                IronRebar: 10,
                QuartzCrystal: 15
            },
            'production': {
                ShatterRebar: 5
            }
        },
        'Silicon Circuit Board': {
            'consumption': {
                CopperSheet: 27.5,
                Silica: 27.5
            },
            'production': {
                CircuitBoard: 12.5
            }
        },
        'Smart Plating': {
            'consumption': {
                ReinforcedIronPlate: 2,
                Rotor: 2
            },
            'production': {
                SmartPlating: 2
            }
        },
        'Stator': {
            'consumption': {
                SteelPipe: 15,
                Wire: 40
            },
            'production': {
                Stator: 5
            }
        },
        'Steel Coated Plate': {
            'consumption': {
                SteelIngot: 7.5,
                Plastic: 5
            },
            'production': {
                IronPlate: 45
            }
        },
        'Steel Rotor': {
            'consumption': {
                SteelPipe: 10,
                Wire: 30
            },
            'production': {
                Rotor: 5
            }
        },
        'Steeled Frame': {
            'consumption': {
                ReinforcedIronPlate: 2,
                SteelPipe: 10
            },
            'production': {
                ModularFrame: 3
            }
        },
        'Stitched Iron Plate': {
            'consumption': {
                IronPlate: 18.75,
                Wire: 37.5
            },
            'production': {
                ReinforcedIronPlate: 5.6
            }
        },
        'Stun Rebar': {
            'consumption': {
                IronRebar: 10,
                Quickwire: 5
            },
            'production': {
                StunRebar: 10
            }
        },
        'Versatile Framework': {
            'consumption': {
                ModularFrame: 2.5,
                SteelBeam: 30
            },
            'production': {
                VersatileFramework: 5
            }
        },
    }


class Blender(Machine):
    recipes = {
        'Battery': {
            'consumption': {
                SulfuricAcid: 50,
                AluminaSolution: 40,
                AluminumCasing: 20
            },
            'production': {
                Battery: 20,
                Water: 30
            }
        },
        'Cooling Device': {
            'consumption': {
                HeatSink: 9.375,
                Motor: 1.875,
                NitrogenGas: 45
            },
            'production': {
                CoolingSystem: 3.8
            }
        },
        'Cooling System': {
            'consumption': {
                HeatSink: 12,
                Rubber: 12,
                Water: 30,
                NitrogenGas: 150
            },
            'production': {
                CoolingSystem: 6
            }
        },
        'Diluted Fuel': {
            'consumption': {
                HeavyOilResidue: 50,
                Water: 100
            },
            'production': {
                Fuel: 100
            }
        },
        'Encased Uranium Cell': {
            'consumption': {
                Uranium: 50,
                Concrete: 15,
                SulfuricAcid: 40
            },
            'production': {
                EncasedUraniumCell: 25,
                SulfuricAcid: 10
            }
        },
        'Fertile Uranium': {
            'consumption': {
                Uranium: 25,
                UraniumWaste: 25,
                NitricAcid: 15,
                SulfuricAcid: 25
            },
            'production': {
                NonFissileUranium: 100,
                Water: 40
            }
        },
        'Fused Modular Frame': {
            'consumption': {
                HeavyModularFrame: 1.5,
                AluminumCasing: 75,
                NitrogenGas: 37.5
            },
            'production': {
                FusedModularFrame: 1.5
            }
        },
        'Heat-Fused Frame': {
            'consumption': {
                HeavyModularFrame: 3,
                AluminumIngot: 150,
                NitricAcid: 24,
                Fuel: 30
            },
            'production': {
                FusedModularFrame: 3
            }
        },
        'Instant Scrap': {
            'consumption': {
                Bauxite: 150,
                Coal: 100,
                SulfuricAcid: 50,
                Water: 60
            },
            'production': {
                AluminumScrap: 300,
                Water: 50
            }
        },
        'Nitric Acid': {
            'consumption': {
                NitrogenGas: 120,
                Water: 30,
                IronPlate: 10
            },
            'production': {
                NitricAcid: 30
            }
        },
        'Non-fissile Uranium': {
            'consumption': {
                UraniumWaste: 37.5,
                Silica: 25,
                NitricAcid: 15,
                SulfuricAcid: 15
            },
            'production': {
                NonFissileUranium: 50,
                Water: 15
            }
        },
        'Turbo Blend Fuel': {
            'consumption': {
                Fuel: 15,
                HeavyOilResidue: 30,
                Sulfur: 22.5,
                PetroleumCoke: 22.5
            },
            'production': {
                Turbofuel: 45
            }
        },
        'Turbo Rifle Ammo': {
            'consumption': {
                RifleAmmo: 125,
                AluminumCasing: 15,
                Turbofuel: 15
            },
            'production': {
                TurboRifleAmmo: 250
            }
        },
    }


class Constructor(Machine):
    recipes = {
        'Alien DNA Capsule': {
            'consumption': {
                AlienProtein: 10
            },
            'production': {
                AlienDNACapsule: 10
            }
        },
        'Aluminum Casing': {
            'consumption': {
                AluminumIngot: 90
            },
            'production': {
                AluminumCasing: 60
            }
        },
        'Biocoal': {
            'consumption': {
                Biomass: 37.5
            },
            'production': {
                Coal: 45
            }
        },
        'Biomass (Alien Protein)': {
            'consumption': {
                AlienProtein: 15
            },
            'production': {
                Biomass: 1500
            }
        },
        'Biomass (Leaves)': {
            'consumption': {
                Leaves: 120
            },
            'production': {
                Biomass: 60
            }
        },
        'Biomass (Alien Mycelia)': {
            'consumption': {
                Mycelia: 150
            },
            'production': {
                Biomass: 150
            }
        },
        'Biomass (Wood)': {
            'consumption': {
                Wood: 60
            },
            'production': {
                Biomass: 300
            }
        },
        'Cable': {
            'consumption': {
                Wire: 60
            },
            'production': {
                Cable: 30
            }
        },
        'Cast Screw': {
            'consumption': {
                IronIngot: 12.5
            },
            'production': {
                Screw: 50
            }
        },
        'Caterium Wire': {
            'consumption': {
                CateriumIngot: 15
            },
            'production': {
                Wire: 120
            }
        },
        'Charcoal': {
            'consumption': {
                Wood: 15
            },
            'production': {
                Coal: 150
            }
        },
        'Color Cartridge': {
            'consumption': {
                FlowerPetals: 50
            },
            'production': {
                ColorCartridge: 100
            }
        },
        'Concrete': {
            'consumption': {
                Limestone: 45
            },
            'production': {
                Concrete: 15
            }
        },
        'Copper Powder': {
            'consumption': {
                CopperIngot: 300
            },
            'production': {
                CopperPowder: 50
            }
        },
        'Copper Sheet': {
            'consumption': {
                CopperIngot: 20
            },
            'production': {
                CopperSheet: 10
            }
        },
        'Empty Canister': {
            'consumption': {
                Plastic: 30
            },
            'production': {
                EmptyCanister: 60
            }
        },
        'Empty Fluid Tank': {
            'consumption': {
                AluminumIngot: 60
            },
            'production': {
                EmptyFluidTank: 60
            }
        },
        'Hatcher Protein': {
            'consumption': {
                HatcherRemains: 20
            },
            'production': {
                AlienProtein: 20
            }
        },
        'Hog Protein': {
            'consumption': {
                HogRemains: 20
            },
            'production': {
                AlienProtein: 20
            }
        },
        'Iron Plate': {
            'consumption': {
                IronIngot: 30
            },
            'production': {
                IronPlate: 20
            }
        },
        'Iron Rebar': {
            'consumption': {
                IronRod: 15
            },
            'production': {
                IronRebar: 15
            }
        },
        'Iron Rod': {
            'consumption': {
                IronIngot: 15
            },
            'production': {
                IronRod: 15
            }
        },
        'Iron Wire': {
            'consumption': {
                IronIngot: 12.5
            },
            'production': {
                Wire: 22.5
            }
        },
        'Power Shard (1)': {
            'consumption': {
                BluePowerSlug: 7.5
            },
            'production': {
                PowerShard: 7.5
            }
        },
        'Power Shard (2)': {
            'consumption': {
                YellowPowerSlug: 5
            },
            'production': {
                PowerShard: 10
            }
        },
        'Power Shard (5)': {
            'consumption': {
                PurplePowerSlug: 2.5
            },
            'production': {
                PowerShard: 12.5
            }
        },
        'Quartz Crystal': {
            'consumption': {
                RawQuartz: 37.5
            },
            'production': {
                QuartzCrystal: 22.5
            }
        },
        'Quickwire': {
            'consumption': {
                CateriumIngot: 12
            },
            'production': {
                Quickwire: 60
            }
        },
        'Screw': {
            'consumption': {
                IronRod: 10
            },
            'production': {
                Screw: 40
            }
        },
        'Silica': {
            'consumption': {
                RawQuartz: 22.5
            },
            'production': {
                Silica: 37.5
            }
        },
        'Solid Biofuel': {
            'consumption': {
                Biomass: 120
            },
            'production': {
                SolidBiofuel: 60
            }
        },
        'Spitter Protein': {
            'consumption': {
                PlasmaSpitterRemains: 20
            },
            'production': {
                AlienProtein: 20
            }
        },
        'Steel Beam': {
            'consumption': {
                SteelIngot: 60
            },
            'production': {
                SteelBeam: 15
            }
        },
        'Steel Canister': {
            'consumption': {
                SteelIngot: 60
            },
            'production': {
                EmptyCanister: 40
            }
        },
        'Steel Pipe': {
            'consumption': {
                SteelIngot: 30
            },
            'production': {
                SteelPipe: 20
            }
        },
        'Steel Rod': {
            'consumption': {
                SteelIngot: 12
            },
            'production': {
                IronRod: 48
            }
        },
        'Steel Screw': {
            'consumption': {
                SteelBeam: 5
            },
            'production': {
                Screw: 260
            }
        },
        'Stinger Protein': {
            'consumption': {
                StingerRemains: 20
            },
            'production': {
                AlienProtein: 20
            }
        },
        'Wire': {
            'consumption': {
                CopperIngot: 15
            },
            'production': {
                Wire: 30
            }
        },
    }


class Foundry(Machine):
    recipes = {
        'Aluminum Ingot': {
            'consumption': {
                AluminumScrap: 90,
                Silica: 75
            },
            'production': {
                AluminumIngot: 60
            }
        },
        'Coke Steel Ingot': {
            'consumption': {
                IronOre: 75,
                PetroleumCoke: 75
            },
            'production': {
                SteelIngot: 100
            }
        },
        'Compacted Steel Ingot': {
            'consumption': {
                IronOre: 22.5,
                CompactedCoal: 11.25
            },
            'production': {
                SteelIngot: 37.5
            }
        },
        'Copper Alloy Ingot': {
            'consumption': {
                CopperOre: 50,
                IronOre: 25
            },
            'production': {
                CopperIngot: 100
            }
        },
        'Iron Alloy Ingot': {
            'consumption': {
                IronOre: 20,
                CopperOre: 20
            },
            'production': {
                IronIngot: 50
            }
        },
        'Solid Steel Ingot': {
            'consumption': {
                IronIngot: 40,
                Coal: 40
            },
            'production': {
                SteelIngot: 60
            }
        },
        'Steel Ingot': {
            'consumption': {
                IronOre: 45,
                Coal: 45
            },
            'production': {
                SteelIngot: 45
            }
        },
    }


class FuelGenerator(Machine):
    recipes = {
        'Fuel': {
            'consumption': {
                Fuel: 12
            },
            'production': {

            }
        },
        'Liquid Biofuel': {
            'consumption': {
                LiquidBiofuel: 12
            },
            'production': {

            }
        },
        'Turbofuel': {
            'consumption': {
                Turbofuel: 4.5
            },
            'production': {

            }
        },
    }

    def __init__(self, recipe_name, clock_speed_modifier=1, allow_undersupply=False):
        super().__init__(recipe_name, clock_speed_modifier)
        self.allow_undersupply = allow_undersupply


class Manufacturer(Machine):
    recipes = {
        'Adaptive Control Unit': {
            'consumption': {
                AutomatedWiring: 7.5,
                CircuitBoard: 5,
                HeavyModularFrame: 1,
                Computer: 1
            },
            'production': {
                AdaptiveControlUnit: 1
            }
        },
        'Automated Miner': {
            'consumption': {
                Motor: 1,
                SteelPipe: 4,
                IronRod: 4,
                IronPlate: 2
            },
            'production': {
                PortableMiner: 1
            }
        },
        'Automated Speed Wiring': {
            'consumption': {
                Stator: 3.75,
                Wire: 75,
                HighSpeedConnector: 1.875
            },
            'production': {
                AutomatedWiring: 7.5
            }
        },
        'Beacon': {
            'consumption': {
                IronPlate: 22.5,
                IronRod: 7.5,
                Wire: 112.5,
                Cable: 15
            },
            'production': {
                Beacon: 7.5
            }
        },
        'Caterium Computer': {
            'consumption': {
                CircuitBoard: 26.25,
                Quickwire: 105,
                Rubber: 45
            },
            'production': {
                Computer: 3.8
            }
        },
        'Classic Battery': {
            'consumption': {
                Sulfur: 45,
                AlcladAluminumSheet: 52.5,
                Plastic: 60,
                Wire: 90
            },
            'production': {
                Battery: 30
            }
        },
        'Computer': {
            'consumption': {
                CircuitBoard: 25,
                Cable: 22.5,
                Plastic: 45,
                Screw: 130
            },
            'production': {
                Computer: 2.5
            }
        },
        'Crystal Beacon': {
            'consumption': {
                SteelBeam: 2,
                SteelPipe: 8,
                CrystalOscillator: 0.5
            },
            'production': {
                Beacon: 10
            }
        },
        'Crystal Oscillator': {
            'consumption': {
                QuartzCrystal: 18,
                Cable: 14,
                ReinforcedIronPlate: 2.5
            },
            'production': {
                CrystalOscillator: 1
            }
        },
        'Explosive Rebar': {
            'consumption': {
                IronRebar: 10,
                SmokelessPowder: 10,
                SteelPipe: 10
            },
            'production': {
                ExplosiveRebar: 5
            }
        },
        'Flexible Framework': {
            'consumption': {
                ModularFrame: 3.75,
                SteelBeam: 22.5,
                Rubber: 30
            },
            'production': {
                VersatileFramework: 7.5
            }
        },
        'Gas Filter': {
            'consumption': {
                Coal: 37.5,
                Rubber: 15,
                Fabric: 15
            },
            'production': {
                GasFilter: 7.5
            }
        },
        'Heavy Encased Frame': {
            'consumption': {
                ModularFrame: 7.5,
                EncasedIndustrialBeam: 9.375,
                SteelPipe: 33.75,
                Concrete: 20.625
            },
            'production': {
                HeavyModularFrame: 2.8
            }
        },
        'Heavy Flexible Frame': {
            'consumption': {
                ModularFrame: 18.75,
                EncasedIndustrialBeam: 11.25,
                Rubber: 75,
                Screw: 390
            },
            'production': {
                HeavyModularFrame: 3.8
            }
        },
        'Heavy Modular Frame': {
            'consumption': {
                ModularFrame: 10,
                SteelPipe: 30,
                EncasedIndustrialBeam: 10,
                Screw: 200
            },
            'production': {
                HeavyModularFrame: 2
            }
        },
        'High-Speed Connector': {
            'consumption': {
                Quickwire: 210,
                Cable: 37.5,
                CircuitBoard: 3.75
            },
            'production': {
                HighSpeedConnector: 3.8
            }
        },
        'Infused Uranium Cell': {
            'consumption': {
                Uranium: 25,
                Silica: 15,
                Sulfur: 25,
                Quickwire: 75
            },
            'production': {
                EncasedUraniumCell: 20
            }
        },
        'Insulated Crystal Oscillator': {
            'consumption': {
                QuartzCrystal: 18.75,
                Rubber: 13.125,
                AILimiter: 1.875
            },
            'production': {
                CrystalOscillator: 1.9
            }
        },
        'Iodine Infused Filter': {
            'consumption': {
                GasFilter: 3.75,
                Quickwire: 30,
                AluminumCasing: 3.75
            },
            'production': {
                IodineInfusedFilter: 3.8
            }
        },
        'Magnetic Field Generator': {
            'consumption': {
                VersatileFramework: 2.5,
                ElectromagneticControlRod: 1,
                Battery: 5
            },
            'production': {
                MagneticFieldGenerator: 1
            }
        },
        'Modular Engine': {
            'consumption': {
                Motor: 2,
                Rubber: 15,
                SmartPlating: 2
            },
            'production': {
                ModularEngine: 1
            }
        },
        'Nuke Nobelisk': {
            'consumption': {
                Nobelisk: 2.5,
                EncasedUraniumCell: 10,
                SmokelessPowder: 5,
                AILimiter: 3
            },
            'production': {
                NukeNobelisk: 0.5
            }
        },
        'Plastic Smart Plating': {
            'consumption': {
                ReinforcedIronPlate: 2.5,
                Rotor: 2.5,
                Plastic: 7.5
            },
            'production': {
                SmartPlating: 5
            }
        },
        'Plutonium Fuel Rod': {
            'consumption': {
                EncasedPlutoniumCell: 7.5,
                SteelBeam: 4.5,
                ElectromagneticControlRod: 1.5,
                HeatSink: 2.5
            },
            'production': {
                PlutoniumFuelRod: 0.3
            }
        },
        'Radio Connection Unit': {
            'consumption': {
                HeatSink: 15,
                HighSpeedConnector: 7.5,
                QuartzCrystal: 45
            },
            'production': {
                RadioControlUnit: 3.8
            }
        },
        'Radio Control System': {
            'consumption': {
                CrystalOscillator: 1.5,
                CircuitBoard: 15,
                AluminumCasing: 90,
                Rubber: 45
            },
            'production': {
                RadioControlUnit: 2.5
            }
        },
        'Radio Control Unit': {
            'consumption': {
                AluminumCasing: 40,
                CrystalOscillator: 1.25,
                Computer: 1.25
            },
            'production': {
                RadioControlUnit: 2.5
            }
        },
        'Rigour Motor': {
            'consumption': {
                Rotor: 3.75,
                Stator: 3.75,
                CrystalOscillator: 1.25
            },
            'production': {
                Motor: 7.5
            }
        },
        'Silicon High-Speeed Connector': {
            'consumption': {
                Quickwire: 90,
                Silica: 37.5,
                CircuitBoard: 3
            },
            'production': {
                HighSpeedConnector: 3
            }
        },
        'Super-State Computer': {
            'consumption': {
                Computer: 3.6,
                ElectromagneticControlRod: 2.4,
                Battery: 24,
                Wire: 54
            },
            'production': {
                Supercomputer: 2.4
            }
        },
        'Supercomputer': {
            'consumption': {
                Computer: 3.75,
                AILimiter: 3.75,
                HighSpeedConnector: 5.625,
                Plastic: 52.5
            },
            'production': {
                Supercomputer: 1.9
            }
        },
        'Thermal Propulsion Rocket': {
            'consumption': {
                ModularEngine: 2.5,
                TurboMotor: 1,
                CoolingSystem: 3,
                FusedModularFrame: 1
            },
            'production': {
                ThermalPropulsionRocket: 1
            }
        },
        'Turbo Electric Motor': {
            'consumption': {
                Motor: 6.5625,
                RadioControlUnit: 8.4375,
                ElectromagneticControlRod: 4.6875,
                Rotor: 6.5625
            },
            'production': {
                TurboMotor: 2.8
            }
        },
        'Turbo Motor': {
            'consumption': {
                CoolingSystem: 7.5,
                RadioControlUnit: 3.75,
                Motor: 7.5,
                Rubber: 45
            },
            'production': {
                TurboMotor: 1.9
            }
        },
        'Turbo Pressure Motor': {
            'consumption': {
                Motor: 7.5,
                PressureConversionCube: 1.875,
                PackagedNitrogenGas: 45,
                Stator: 15
            },
            'production': {
                TurboMotor: 3.8
            }
        },
        'Turbo Rifle Ammo': {
            'consumption': {
                RifleAmmo: 125,
                AluminumCasing: 15,
                PackagedTurboFuel: 15
            },
            'production': {
                TurboRifleAmmo: 250
            }
        },
        'Uranium Fuel Rod': {
            'consumption': {
                EncasedUraniumCell: 20,
                EncasedIndustrialBeam: 1.2,
                ElectromagneticControlRod: 2
            },
            'production': {
                UraniumFuelRod: 0.4
            }
        },

        'Uranium Fuel Unit': {
            'consumption': {
                EncasedUraniumCell: 20,
                ElectromagneticControlRod: 2,
                CrystalOscillator: 0.6,
                Beacon: 1.2
            },
            'production': {
                UraniumFuelRod: 0.6
            }
        },
    }


class Refinery(Machine):
    recipes = {
        'Alumina Solution': {
            'consumption': {
                Bauxite: 120,
                Water: 180
            },
            'production': {
                AluminaSolution: 120,
                Silica: 50
            }
        },
        'Aluminum Scrap': {
            'consumption': {
                AluminaSolution: 240,
                Coal: 120
            },
            'production': {
                AluminumScrap: 360,
                Water: 120
            }
        },
        'Coated Cable': {
            'consumption': {
                Wire: 37.5,
                HeavyOilResidue: 15
            },
            'production': {
                Cable: 67.5
            }
        },
        'Diluted Packaged Fuel': {
            'consumption': {
                HeavyOilResidue: 30,
                PackagedWater: 60
            },
            'production': {
                PackagedFuel: 60
            }
        },
        'Electrode-Aluminum Scrap': {
            'consumption': {
                AluminaSolution: 180,
                PetroleumCoke: 60
            },
            'production': {
                AluminumScrap: 300,
                Water: 105
            }
        },
        'Fuel': {
            'consumption': {
                CrudeOil: 60
            },
            'production': {
                Fuel: 40,
                PolymerResin: 30
            }
        },
        'Heavy Oil Residue': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                HeavyOilResidue: 40,
                PolymerResin: 20
            }
        },
        'Liquid Biofuel': {
            'consumption': {
                SolidBiofuel: 990,
                Water: 45
            },
            'production': {
                LiquidBiofuel: 60
            }
        },
        'Petroleum Coke': {
            'consumption': {
                HeavyOilResidue: 40
            },
            'production': {
                PetroleumCoke: 120
            }
        },
        'Plastic': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                Plastic: 20,
                HeavyOilResidue: 10
            }
        },
        'Polyester Fabric': {
            'consumption': {
                PolymerResin: 30,
                Water: 30
            },
            'production': {
                Fabric: 30
            }
        },
        'Polymer Resin': {
            'consumption': {
                CrudeOil: 60
            },
            'production': {
                PolymerResin: 130,
                HeavyOilResidue: 20
            }
        },
        'Pure Caterium Ingot': {
            'consumption': {
                CateriumOre: 24,
                Water: 24
            },
            'production': {
                CateriumIngot: 12
            }
        },
        'Pure Copper Ingot': {
            'consumption': {
                CopperOre: 15,
                Water: 10
            },
            'production': {
                CopperIngot: 37.5
            }
        },
        'Pure Iron Ingot': {
            'consumption': {
                IronOre: 35,
                Water: 20
            },
            'production': {
                IronIngot: 65
            }
        },
        'Pure Quartz Crystal': {
            'consumption': {
                RawQuartz: 67.5,
                Water: 37.5
            },
            'production': {
                QuartzCrystal: 52.5
            }
        },
        'Recycled Plastic': {
            'consumption': {
                Rubber: 30,
                Fuel: 30
            },
            'production': {
                Plastic: 60
            }
        },
        'Recycled Rubber': {
            'consumption': {
                Plastic: 30,
                Fuel: 30
            },
            'production': {
                Rubber: 60
            }
        },
        'Residual Fuel': {
            'consumption': {
                HeavyOilResidue: 60
            },
            'production': {
                Fuel: 40
            }
        },
        'Residual Plastic': {
            'consumption': {
                PolymerResin: 60,
                Water: 20
            },
            'production': {
                Plastic: 20
            }
        },
        'Residual Rubber': {
            'consumption': {
                PolymerResin: 40,
                Water: 40
            },
            'production': {
                Rubber: 20
            }
        },
        'Rubber': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                Rubber: 20,
                HeavyOilResidue: 20
            }
        },
        'Sloppy Alumina': {
            'consumption': {
                Bauxite: 200,
                Water: 200
            },
            'production': {
                AluminaSolution: 240
            }
        },
        'Smokeless Powder': {
            'consumption': {
                BlackPowder: 20,
                HeavyOilResidue: 10
            },
            'production': {
                SmokelessPowder: 20
            }
        },
        'Steamed Copper Sheet': {
            'consumption': {
                CopperIngot: 22.5,
                Water: 22.5
            },
            'production': {
                CopperSheet: 22.5
            }
        },
        'Sulfuric Acid': {
            'consumption': {
                Sulfur: 50,
                Water: 50
            },
            'production': {
                SulfuricAcid: 50
            }
        },
        'Turbo Heavy Fuel': {
            'consumption': {
                HeavyOilResidue: 37.5,
                CompactedCoal: 30
            },
            'production': {
                Turbofuel: 30
            }
        },
        'TurboFuel': {
            'consumption': {
                Fuel: 22.5,
                CompactedCoal: 15
            },
            'production': {
                Turbofuel: 18.8
            }
        },
        'Wet Concrete': {
            'consumption': {
                Limestone: 120,
                Water: 100
            },
            'production': {
                Concrete: 80
            }
        },
    }


class Smelter(Machine):
    recipes = {
        'Caterium Ingot': {
            'consumption': {
                CateriumOre: 45
            },
            'production': {
                CateriumIngot: 15
            }
        },
        'Copper Ingot': {
            'consumption': {
                CopperOre: 30
            },
            'production': {
                CopperIngot: 30
            }
        },
        'Iron Ingot': {
            'consumption': {
                IronOre: 30
            },
            'production': {
                IronIngot: 30
            }
        },
        'Pure Aluminum Ingot': {
            'consumption': {
                AluminumScrap: 30
            },
            'production': {
                AluminumIngot: 30
            }
        }
    }
