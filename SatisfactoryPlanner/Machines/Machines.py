from ..Resource.Resource import *


class Machine:
    def __init__(self, recipe_name):
        self.consumption_rates = self.recipes[recipe_name]["consumption"]
        self.production_rates = self.recipes[recipe_name]["production"]

    def get_consumption_rate(self):
        return self.consumption_rates

    def get_production_rates(self):
        return self.production_rates


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
