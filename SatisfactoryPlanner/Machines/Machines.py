from ..Resource.Oil import CrudeOil
from ..Resource.Ore import Bauxite, CateriumOre, Coal, CopperOre, IronOre, Limestone, NitrogenGas, RawQuartz, Sulfur, Uranium
from ..Resource import Resource


class Machine:
    recipes = {
        'Example Recipe': {
            'consumption': {
                IronOre: 1
            },
            'production': {
                Resource.IronIngot: 1
            }
        }
    }

    def __init__(self, recipe_name, clock_speed_modifier=1):
        if clock_speed_modifier > 2.5 or clock_speed_modifier < .25:
            raise ValueError('Invalid clock speed percentage!')

        self.consumption_rates = {resource: round(rate * clock_speed_modifier, 4) for resource, rate in
                                  self.recipes[recipe_name]["consumption"].items()}
        self.production_rates = {resource: round(rate * clock_speed_modifier, 4) for resource, rate in
                                 self.recipes[recipe_name]["production"].items()}

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
                Resource.IronPlate: 11.25,
                Resource.Rubber: 3.75
            },
            'production': {
                Resource.ReinforcedIronPlate: 3.8
            }
        },
        'AI Limiter': {
            'consumption': {
                Resource.CopperSheet: 25,
                Resource.Quickwire: 100
            },
            'production': {
                Resource.AILimiter: 5
            }
        },
        'Alclad Aluminum Sheet': {
            'consumption': {
                Resource.AluminumIngot: 30,
                Resource.CopperIngot: 10
            },
            'production': {
                Resource.AlcladAluminumSheet: 30
            }
        },
        'Alclad Casing': {
            'consumption': {
                Resource.AluminumIngot: 150,
                Resource.CopperIngot: 75
            },
            'production': {
                Resource.AluminumCasing: 112.5
            }
        },
        'Assembly Director System': {
            'consumption': {
                Resource.AdaptiveControlUnit: 1.5,
                Resource.Supercomputer: 0.75
            },
            'production': {
                Resource.AssemblyDirectorSystem: 0.8
            }
        },
        'Automated Wiring': {
            'consumption': {
                Resource.Stator: 2.5,
                Resource.Cable: 50
            },
            'production': {
                Resource.AutomatedWiring: 2.5
            }
        },
        'Black Powder': {
            'consumption': {
                Coal: 15,
                Sulfur: 15
            },
            'production': {
                Resource.BlackPowder: 30
            }
        },
        'Bolted Frame': {
            'consumption': {
                Resource.ReinforcedIronPlate: 7.5,
                Resource.Screw: 140
            },
            'production': {
                Resource.ModularFrame: 5
            }
        },
        'Bolted Iron Plate': {
            'consumption': {
                Resource.IronPlate: 90,
                Resource.Screw: 250
            },
            'production': {
                Resource.ReinforcedIronPlate: 15
            }
        },
        'Caterium Circuit Board': {
            'consumption': {
                Resource.Plastic: 12.5,
                Resource.Quickwire: 37.5
            },
            'production': {
                Resource.CircuitBoard: 8.8
            }
        },
        'Cheap Silica': {
            'consumption': {
                RawQuartz: 11.25,
                Limestone: 18.75
            },
            'production': {
                Resource.Silica: 26.3
            }
        },
        'Circuit Board': {
            'consumption': {
                Resource.CopperSheet: 15,
                Resource.Plastic: 30
            },
            'production': {
                Resource.CircuitBoard: 7.5
            }
        },
        'Cluster Nobelisk': {
            'consumption': {
                Resource.Nobelisk: 7.5,
                Resource.SmokelessPowder: 10
            },
            'production': {
                Resource.ClusterNobelisk: 2.5
            }
        },
        'Coated Iron Canister': {
            'consumption': {
                Resource.IronPlate: 30,
                Resource.CopperSheet: 15
            },
            'production': {
                Resource.EmptyCanister: 60
            }
        },
        'Coated Iron Plate': {
            'consumption': {
                Resource.IronIngot: 50,
                Resource.Plastic: 10
            },
            'production': {
                Resource.IronPlate: 75
            }
        },
        'Compacted Coal': {
            'consumption': {
                Coal: 25,
                Sulfur: 25
            },
            'production': {
                Resource.CompactedCoal: 25
            }
        },
        'Copper Rotor': {
            'consumption': {
                Resource.CopperSheet: 22.5,
                Resource.Screw: 195
            },
            'production': {
                Resource.Rotor: 11.3
            }
        },
        'Crystal Computer': {
            'consumption': {
                Resource.CircuitBoard: 7.5,
                Resource.CrystalOscillator: 2.8125
            },
            'production': {
                Resource.Computer: 2.8
            }
        },
        'Electric Motor': {
            'consumption': {
                Resource.ElectromagneticControlRod: 3.75,
                Resource.Rotor: 7.5
            },
            'production': {
                Resource.Motor: 7.5
            }
        },
        'Electrode Circuit Board': {
            'consumption': {
                Resource.Rubber: 30,
                Resource.PetroleumCoke: 45
            },
            'production': {
                Resource.CircuitBoard: 5
            }
        },
        'Electromagnetic Connection Rod': {
            'consumption': {
                Resource.Stator: 8,
                Resource.HighSpeedConnector: 4
            },
            'production': {
                Resource.ElectromagneticControlRod: 8
            }
        },
        'Electromagnetic Control Rod': {
            'consumption': {
                Resource.Stator: 6,
                Resource.AILimiter: 4
            },
            'production': {
                Resource.ElectromagneticControlRod: 4
            }
        },
        'Encased Industrial Beam': {
            'consumption': {
                Resource.SteelBeam: 24,
                Resource.Concrete: 30
            },
            'production': {
                Resource.EncasedIndustrialBeam: 6
            }
        },
        'Encased Industrial Pipe': {
            'consumption': {
                Resource.SteelPipe: 28,
                Resource.Concrete: 20
            },
            'production': {
                Resource.EncasedIndustrialBeam: 4
            }
        },
        'Encased Plutonium Cell': {
            'consumption': {
                Resource.PlutoniumPellet: 10,
                Resource.Concrete: 20
            },
            'production': {
                Resource.EncasedPlutoniumCell: 5
            }
        },
        'Fabric': {
            'consumption': {
                Resource.Mycelia: 15,
                Resource.Biomass: 75
            },
            'production': {
                Resource.Fabric: 15
            }
        },
        'Fine Black Powder': {
            'consumption': {
                Sulfur: 7.5,
                Resource.CompactedCoal: 3.75
            },
            'production': {
                Resource.BlackPowder: 15
            }
        },
        'Fine Concrete': {
            'consumption': {
                Resource.Silica: 7.5,
                Limestone: 30
            },
            'production': {
                Resource.Concrete: 25
            }
        },
        'Fused Quickwire': {
            'consumption': {
                Resource.CateriumIngot: 7.5,
                Resource.CopperIngot: 37.5
            },
            'production': {
                Resource.Quickwire: 90
            }
        },
        'Fused Wire': {
            'consumption': {
                Resource.CopperIngot: 12,
                Resource.CateriumIngot: 3
            },
            'production': {
                Resource.Wire: 90
            }
        },
        'Gas Nobelisk': {
            'consumption': {
                Resource.Nobelisk: 5,
                Resource.Biomass: 50
            },
            'production': {
                Resource.GasNobelisk: 5
            }
        },
        'Heat Exchanger': {
            'consumption': {
                Resource.AluminumCasing: 30,
                Resource.Rubber: 30
            },
            'production': {
                Resource.HeatSink: 10
            }
        },
        'Heat Sink': {
            'consumption': {
                Resource.AlcladAluminumSheet: 37.5,
                Resource.CopperSheet: 22.5
            },
            'production': {
                Resource.HeatSink: 7.5
            }
        },
        'Homing Riffle Ammo': {
            'consumption': {
                Resource.RifleAmmo: 50,
                Resource.HighSpeedConnector: 2.5
            },
            'production': {
                Resource.HomingRifleAmmo: 25
            }
        },
        'Insulated Cable': {
            'consumption': {
                Resource.Wire: 45,
                Resource.Rubber: 30
            },
            'production': {
                Resource.Cable: 100
            }
        },
        'Modular Frame': {
            'consumption': {
                Resource.ReinforcedIronPlate: 3,
                Resource.IronRod: 12
            },
            'production': {
                Resource.ModularFrame: 2
            }
        },
        'Motor': {
            'consumption': {
                Resource.Rotor: 10,
                Resource.Stator: 10
            },
            'production': {
                Resource.Motor: 5
            }
        },
        'Nobelisk': {
            'consumption': {
                Resource.SteelPipe: 20,
                Resource.BlackPowder: 20
            },
            'production': {
                Resource.Nobelisk: 10
            }
        },
        'OC Supercomputer': {
            'consumption': {
                Resource.RadioControlUnit: 9,
                Resource.CoolingSystem: 9
            },
            'production': {
                Resource.Supercomputer: 3
            }
        },
        'Plutonium Fuel Unit': {
            'consumption': {
                Resource.EncasedPlutoniumCell: 10,
                Resource.PressureConversionCube: 0.5
            },
            'production': {
                Resource.PlutoniumFuelRod: 0.5
            }
        },
        'Pressure Conversion Cube': {
            'consumption': {
                Resource.FusedModularFrame: 1,
                Resource.RadioControlUnit: 2
            },
            'production': {
                Resource.PressureConversionCube: 1
            }
        },
        'Pulse Nobelisk': {
            'consumption': {
                Resource.Nobelisk: 5,
                Resource.CrystalOscillator: 1
            },
            'production': {
                Resource.PulseNobelisk: 5
            }
        },
        'Quickwire Cable': {
            'consumption': {
                Resource.Quickwire: 7.5,
                Resource.Rubber: 5
            },
            'production': {
                Resource.Cable: 27.5
            }
        },
        'Quickwire Stator': {
            'consumption': {
                Resource.SteelPipe: 16,
                Resource.Quickwire: 60
            },
            'production': {
                Resource.Stator: 2
            }
        },
        'Reinforced Iron Plate': {
            'consumption': {
                Resource.IronPlate: 30,
                Resource.Screw: 60
            },
            'production': {
                Resource.ReinforcedIronPlate: 5
            }
        },
        'Rifle Ammo': {
            'consumption': {
                Resource.CopperSheet: 15,
                Resource.SmokelessPowder: 10
            },
            'production': {
                Resource.RifleAmmo: 75
            }
        },
        'Rotor': {
            'consumption': {
                Resource.IronRod: 20,
                Resource.Screw: 100
            },
            'production': {
                Resource.Rotor: 4
            }
        },
        'Rubber Concrete': {
            'consumption': {
                Limestone: 50,
                Resource.Rubber: 10
            },
            'production': {
                Resource.Concrete: 45
            }
        },
        'Shatter Rebar': {
            'consumption': {
                Resource.IronRebar: 10,
                Resource.QuartzCrystal: 15
            },
            'production': {
                Resource.ShatterRebar: 5
            }
        },
        'Silicon Circuit Board': {
            'consumption': {
                Resource.CopperSheet: 27.5,
                Resource.Silica: 27.5
            },
            'production': {
                Resource.CircuitBoard: 12.5
            }
        },
        'Smart Plating': {
            'consumption': {
                Resource.ReinforcedIronPlate: 2,
                Resource.Rotor: 2
            },
            'production': {
                Resource.SmartPlating: 2
            }
        },
        'Stator': {
            'consumption': {
                Resource.SteelPipe: 15,
                Resource.Wire: 40
            },
            'production': {
                Resource.Stator: 5
            }
        },
        'Steel Coated Plate': {
            'consumption': {
                Resource.SteelIngot: 7.5,
                Resource.Plastic: 5
            },
            'production': {
                Resource.IronPlate: 45
            }
        },
        'Steel Rotor': {
            'consumption': {
                Resource.SteelPipe: 10,
                Resource.Wire: 30
            },
            'production': {
                Resource.Rotor: 5
            }
        },
        'Steeled Frame': {
            'consumption': {
                Resource.ReinforcedIronPlate: 2,
                Resource.SteelPipe: 10
            },
            'production': {
                Resource.ModularFrame: 3
            }
        },
        'Stitched Iron Plate': {
            'consumption': {
                Resource.IronPlate: 18.75,
                Resource.Wire: 37.5
            },
            'production': {
                Resource.ReinforcedIronPlate: 5.6
            }
        },
        'Stun Rebar': {
            'consumption': {
                Resource.IronRebar: 10,
                Resource.Quickwire: 5
            },
            'production': {
                Resource.StunRebar: 10
            }
        },
        'Versatile Framework': {
            'consumption': {
                Resource.ModularFrame: 2.5,
                Resource.SteelBeam: 30
            },
            'production': {
                Resource.VersatileFramework: 5
            }
        },
    }


class Blender(Machine):
    recipes = {
        'Battery': {
            'consumption': {
                Resource.SulfuricAcid: 50,
                Resource.AluminaSolution: 40,
                Resource.AluminumCasing: 20
            },
            'production': {
                Resource.Battery: 20,
                Resource.Water: 30
            }
        },
        'Cooling Device': {
            'consumption': {
                Resource.HeatSink: 9.375,
                Resource.Motor: 1.875,
                NitrogenGas: 45
            },
            'production': {
                Resource.CoolingSystem: 3.8
            }
        },
        'Cooling System': {
            'consumption': {
                Resource.HeatSink: 12,
                Resource.Rubber: 12,
                Resource.Water: 30,
                NitrogenGas: 150
            },
            'production': {
                Resource.CoolingSystem: 6
            }
        },
        'Diluted Fuel': {
            'consumption': {
                Resource.HeavyOilResidue: 50,
                Resource.Water: 100
            },
            'production': {
                Resource.Fuel: 100
            }
        },
        'Encased Uranium Cell': {
            'consumption': {
                Uranium: 50,
                Resource.Concrete: 15,
                Resource.SulfuricAcid: 40
            },
            'production': {
                Resource.EncasedUraniumCell: 25,
                Resource.SulfuricAcid: 10
            }
        },
        'Fertile Uranium': {
            'consumption': {
                Uranium: 25,
                Resource.UraniumWaste: 25,
                Resource.NitricAcid: 15,
                Resource.SulfuricAcid: 25
            },
            'production': {
                Resource.NonFissileUranium: 100,
                Resource.Water: 40
            }
        },
        'Fused Modular Frame': {
            'consumption': {
                Resource.HeavyModularFrame: 1.5,
                Resource.AluminumCasing: 75,
                NitrogenGas: 37.5
            },
            'production': {
                Resource.FusedModularFrame: 1.5
            }
        },
        'Heat-Fused Frame': {
            'consumption': {
                Resource.HeavyModularFrame: 3,
                Resource.AluminumIngot: 150,
                Resource.NitricAcid: 24,
                Resource.Fuel: 30
            },
            'production': {
                Resource.FusedModularFrame: 3
            }
        },
        'Instant Scrap': {
            'consumption': {
                Bauxite: 150,
                Coal: 100,
                Resource.SulfuricAcid: 50,
                Resource.Water: 60
            },
            'production': {
                Resource.AluminumScrap: 300,
                Resource.Water: 50
            }
        },
        'Nitric Acid': {
            'consumption': {
                NitrogenGas: 120,
                Resource.Water: 30,
                Resource.IronPlate: 10
            },
            'production': {
                Resource.NitricAcid: 30
            }
        },
        'Non-fissile Uranium': {
            'consumption': {
                Resource.UraniumWaste: 37.5,
                Resource.Silica: 25,
                Resource.NitricAcid: 15,
                Resource.SulfuricAcid: 15
            },
            'production': {
                Resource.NonFissileUranium: 50,
                Resource.Water: 15
            }
        },
        'Turbo Blend Fuel': {
            'consumption': {
                Resource.Fuel: 15,
                Resource.HeavyOilResidue: 30,
                Sulfur: 22.5,
                Resource.PetroleumCoke: 22.5
            },
            'production': {
                Resource.Turbofuel: 45
            }
        },
        'Turbo Rifle Ammo': {
            'consumption': {
                Resource.RifleAmmo: 125,
                Resource.AluminumCasing: 15,
                Resource.Turbofuel: 15
            },
            'production': {
                Resource.TurboRifleAmmo: 250
            }
        },
    }


class Constructor(Machine):
    recipes = {
        'Alien DNA Capsule': {
            'consumption': {
                Resource.AlienProtein: 10
            },
            'production': {
                Resource.AlienDNACapsule: 10
            }
        },
        'Aluminum Casing': {
            'consumption': {
                Resource.AluminumIngot: 90
            },
            'production': {
                Resource.AluminumCasing: 60
            }
        },
        'Biocoal': {
            'consumption': {
                Resource.Biomass: 37.5
            },
            'production': {
                Coal: 45
            }
        },
        'Biomass (Alien Protein)': {
            'consumption': {
                Resource.AlienProtein: 15
            },
            'production': {
                Resource.Biomass: 1500
            }
        },
        'Biomass (Leaves)': {
            'consumption': {
                Resource.Leaves: 120
            },
            'production': {
                Resource.Biomass: 60
            }
        },
        'Biomass (Alien Mycelia)': {
            'consumption': {
                Resource.Mycelia: 150
            },
            'production': {
                Resource.Biomass: 150
            }
        },
        'Biomass (Wood)': {
            'consumption': {
                Resource.Wood: 60
            },
            'production': {
                Resource.Biomass: 300
            }
        },
        'Cable': {
            'consumption': {
                Resource.Wire: 60
            },
            'production': {
                Resource.Cable: 30
            }
        },
        'Cast Screw': {
            'consumption': {
                Resource.IronIngot: 12.5
            },
            'production': {
                Resource.Screw: 50
            }
        },
        'Caterium Wire': {
            'consumption': {
                Resource.CateriumIngot: 15
            },
            'production': {
                Resource.Wire: 120
            }
        },
        'Charcoal': {
            'consumption': {
                Resource.Wood: 15
            },
            'production': {
                Coal: 150
            }
        },
        'Color Cartridge': {
            'consumption': {
                Resource.FlowerPetals: 50
            },
            'production': {
                Resource.ColorCartridge: 100
            }
        },
        'Concrete': {
            'consumption': {
                Limestone: 45
            },
            'production': {
                Resource.Concrete: 15
            }
        },
        'Copper Powder': {
            'consumption': {
                Resource.CopperIngot: 300
            },
            'production': {
                Resource.CopperPowder: 50
            }
        },
        'Copper Sheet': {
            'consumption': {
                Resource.CopperIngot: 20
            },
            'production': {
                Resource.CopperSheet: 10
            }
        },
        'Empty Canister': {
            'consumption': {
                Resource.Plastic: 30
            },
            'production': {
                Resource.EmptyCanister: 60
            }
        },
        'Empty Fluid Tank': {
            'consumption': {
                Resource.AluminumIngot: 60
            },
            'production': {
                Resource.EmptyFluidTank: 60
            }
        },
        'Hatcher Protein': {
            'consumption': {
                Resource.HatcherRemains: 20
            },
            'production': {
                Resource.AlienProtein: 20
            }
        },
        'Hog Protein': {
            'consumption': {
                Resource.HogRemains: 20
            },
            'production': {
                Resource.AlienProtein: 20
            }
        },
        'Iron Plate': {
            'consumption': {
                Resource.IronIngot: 30
            },
            'production': {
                Resource.IronPlate: 20
            }
        },
        'Iron Rebar': {
            'consumption': {
                Resource.IronRod: 15
            },
            'production': {
                Resource.IronRebar: 15
            }
        },
        'Iron Rod': {
            'consumption': {
                Resource.IronIngot: 15
            },
            'production': {
                Resource.IronRod: 15
            }
        },
        'Iron Wire': {
            'consumption': {
                Resource.IronIngot: 12.5
            },
            'production': {
                Resource.Wire: 22.5
            }
        },
        'Power Shard (1)': {
            'consumption': {
                Resource.BluePowerSlug: 7.5
            },
            'production': {
                Resource.PowerShard: 7.5
            }
        },
        'Power Shard (2)': {
            'consumption': {
                Resource.YellowPowerSlug: 5
            },
            'production': {
                Resource.PowerShard: 10
            }
        },
        'Power Shard (5)': {
            'consumption': {
                Resource.PurplePowerSlug: 2.5
            },
            'production': {
                Resource.PowerShard: 12.5
            }
        },
        'Quartz Crystal': {
            'consumption': {
                RawQuartz: 37.5
            },
            'production': {
                Resource.QuartzCrystal: 22.5
            }
        },
        'Quickwire': {
            'consumption': {
                Resource.CateriumIngot: 12
            },
            'production': {
                Resource.Quickwire: 60
            }
        },
        'Screw': {
            'consumption': {
                Resource.IronRod: 10
            },
            'production': {
                Resource.Screw: 40
            }
        },
        'Silica': {
            'consumption': {
                RawQuartz: 22.5
            },
            'production': {
                Resource.Silica: 37.5
            }
        },
        'Solid Biofuel': {
            'consumption': {
                Resource.Biomass: 120
            },
            'production': {
                Resource.SolidBiofuel: 60
            }
        },
        'Spitter Protein': {
            'consumption': {
                Resource.PlasmaSpitterRemains: 20
            },
            'production': {
                Resource.AlienProtein: 20
            }
        },
        'Steel Beam': {
            'consumption': {
                Resource.SteelIngot: 60
            },
            'production': {
                Resource.SteelBeam: 15
            }
        },
        'Steel Canister': {
            'consumption': {
                Resource.SteelIngot: 60
            },
            'production': {
                Resource.EmptyCanister: 40
            }
        },
        'Steel Pipe': {
            'consumption': {
                Resource.SteelIngot: 30
            },
            'production': {
                Resource.SteelPipe: 20
            }
        },
        'Steel Rod': {
            'consumption': {
                Resource.SteelIngot: 12
            },
            'production': {
                Resource.IronRod: 48
            }
        },
        'Steel Screw': {
            'consumption': {
                Resource.SteelBeam: 5
            },
            'production': {
                Resource.Screw: 260
            }
        },
        'Stinger Protein': {
            'consumption': {
                Resource.StingerRemains: 20
            },
            'production': {
                Resource.AlienProtein: 20
            }
        },
        'Wire': {
            'consumption': {
                Resource.CopperIngot: 15
            },
            'production': {
                Resource.Wire: 30
            }
        },
    }


class Foundry(Machine):
    recipes = {
        'Aluminum Ingot': {
            'consumption': {
                Resource.AluminumScrap: 90,
                Resource.Silica: 75
            },
            'production': {
                Resource.AluminumIngot: 60
            }
        },
        'Coke Steel Ingot': {
            'consumption': {
                IronOre: 75,
                Resource.PetroleumCoke: 75
            },
            'production': {
                Resource.SteelIngot: 100
            }
        },
        'Compacted Steel Ingot': {
            'consumption': {
                IronOre: 22.5,
                Resource.CompactedCoal: 11.25
            },
            'production': {
                Resource.SteelIngot: 37.5
            }
        },
        'Copper Alloy Ingot': {
            'consumption': {
                CopperOre: 50,
                IronOre: 25
            },
            'production': {
                Resource.CopperIngot: 100
            }
        },
        'Iron Alloy Ingot': {
            'consumption': {
                IronOre: 20,
                CopperOre: 20
            },
            'production': {
                Resource.IronIngot: 50
            }
        },
        'Solid Steel Ingot': {
            'consumption': {
                Resource.IronIngot: 40,
                Coal: 40
            },
            'production': {
                Resource.SteelIngot: 60
            }
        },
        'Steel Ingot': {
            'consumption': {
                IronOre: 45,
                Coal: 45
            },
            'production': {
                Resource.SteelIngot: 45
            }
        },
    }


class FuelGenerator(Machine):
    recipes = {
        'Fuel': {
            'consumption': {
                Resource.Fuel: 12
            },
            'production': {

            }
        },
        'Liquid Biofuel': {
            'consumption': {
                Resource.LiquidBiofuel: 12
            },
            'production': {

            }
        },
        'Turbofuel': {
            'consumption': {
                Resource.Turbofuel: 4.5
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
                Resource.AutomatedWiring: 7.5,
                Resource.CircuitBoard: 5,
                Resource.HeavyModularFrame: 1,
                Resource.Computer: 1
            },
            'production': {
                Resource.AdaptiveControlUnit: 1
            }
        },
        'Automated Miner': {
            'consumption': {
                Resource.Motor: 1,
                Resource.SteelPipe: 4,
                Resource.IronRod: 4,
                Resource.IronPlate: 2
            },
            'production': {
                Resource.PortableMiner: 1
            }
        },
        'Automated Speed Wiring': {
            'consumption': {
                Resource.Stator: 3.75,
                Resource.Wire: 75,
                Resource.HighSpeedConnector: 1.875
            },
            'production': {
                Resource.AutomatedWiring: 7.5
            }
        },
        'Beacon': {
            'consumption': {
                Resource.IronPlate: 22.5,
                Resource.IronRod: 7.5,
                Resource.Wire: 112.5,
                Resource.Cable: 15
            },
            'production': {
                Resource.Beacon: 7.5
            }
        },
        'Caterium Computer': {
            'consumption': {
                Resource.CircuitBoard: 26.25,
                Resource.Quickwire: 105,
                Resource.Rubber: 45
            },
            'production': {
                Resource.Computer: 3.8
            }
        },
        'Classic Battery': {
            'consumption': {
                Sulfur: 45,
                Resource.AlcladAluminumSheet: 52.5,
                Resource.Plastic: 60,
                Resource.Wire: 90
            },
            'production': {
                Resource.Battery: 30
            }
        },
        'Computer': {
            'consumption': {
                Resource.CircuitBoard: 25,
                Resource.Cable: 22.5,
                Resource.Plastic: 45,
                Resource.Screw: 130
            },
            'production': {
                Resource.Computer: 2.5
            }
        },
        'Crystal Beacon': {
            'consumption': {
                Resource.SteelBeam: 2,
                Resource.SteelPipe: 8,
                Resource.CrystalOscillator: 0.5
            },
            'production': {
                Resource.Beacon: 10
            }
        },
        'Crystal Oscillator': {
            'consumption': {
                Resource.QuartzCrystal: 18,
                Resource.Cable: 14,
                Resource.ReinforcedIronPlate: 2.5
            },
            'production': {
                Resource.CrystalOscillator: 1
            }
        },
        'Explosive Rebar': {
            'consumption': {
                Resource.IronRebar: 10,
                Resource.SmokelessPowder: 10,
                Resource.SteelPipe: 10
            },
            'production': {
                Resource.ExplosiveRebar: 5
            }
        },
        'Flexible Framework': {
            'consumption': {
                Resource.ModularFrame: 3.75,
                Resource.SteelBeam: 22.5,
                Resource.Rubber: 30
            },
            'production': {
                Resource.VersatileFramework: 7.5
            }
        },
        'Gas Filter': {
            'consumption': {
                Coal: 37.5,
                Resource.Rubber: 15,
                Resource.Fabric: 15
            },
            'production': {
                Resource.GasFilter: 7.5
            }
        },
        'Heavy Encased Frame': {
            'consumption': {
                Resource.ModularFrame: 7.5,
                Resource.EncasedIndustrialBeam: 9.375,
                Resource.SteelPipe: 33.75,
                Resource.Concrete: 20.625
            },
            'production': {
                Resource.HeavyModularFrame: 2.8
            }
        },
        'Heavy Flexible Frame': {
            'consumption': {
                Resource.ModularFrame: 18.75,
                Resource.EncasedIndustrialBeam: 11.25,
                Resource.Rubber: 75,
                Resource.Screw: 390
            },
            'production': {
                Resource.HeavyModularFrame: 3.8
            }
        },
        'Heavy Modular Frame': {
            'consumption': {
                Resource.ModularFrame: 10,
                Resource.SteelPipe: 30,
                Resource.EncasedIndustrialBeam: 10,
                Resource.Screw: 200
            },
            'production': {
                Resource.HeavyModularFrame: 2
            }
        },
        'High-Speed Connector': {
            'consumption': {
                Resource.Quickwire: 210,
                Resource.Cable: 37.5,
                Resource.CircuitBoard: 3.75
            },
            'production': {
                Resource.HighSpeedConnector: 3.8
            }
        },
        'Infused Uranium Cell': {
            'consumption': {
                Uranium: 25,
                Resource.Silica: 15,
                Sulfur: 25,
                Resource.Quickwire: 75
            },
            'production': {
                Resource.EncasedUraniumCell: 20
            }
        },
        'Insulated Crystal Oscillator': {
            'consumption': {
                Resource.QuartzCrystal: 18.75,
                Resource.Rubber: 13.125,
                Resource.AILimiter: 1.875
            },
            'production': {
                Resource.CrystalOscillator: 1.9
            }
        },
        'Iodine Infused Filter': {
            'consumption': {
                Resource.GasFilter: 3.75,
                Resource.Quickwire: 30,
                Resource.AluminumCasing: 3.75
            },
            'production': {
                Resource.IodineInfusedFilter: 3.8
            }
        },
        'Magnetic Field Generator': {
            'consumption': {
                Resource.VersatileFramework: 2.5,
                Resource.ElectromagneticControlRod: 1,
                Resource.Battery: 5
            },
            'production': {
                Resource.MagneticFieldGenerator: 1
            }
        },
        'Modular Engine': {
            'consumption': {
                Resource.Motor: 2,
                Resource.Rubber: 15,
                Resource.SmartPlating: 2
            },
            'production': {
                Resource.ModularEngine: 1
            }
        },
        'Nuke Nobelisk': {
            'consumption': {
                Resource.Nobelisk: 2.5,
                Resource.EncasedUraniumCell: 10,
                Resource.SmokelessPowder: 5,
                Resource.AILimiter: 3
            },
            'production': {
                Resource.NukeNobelisk: 0.5
            }
        },
        'Plastic Smart Plating': {
            'consumption': {
                Resource.ReinforcedIronPlate: 2.5,
                Resource.Rotor: 2.5,
                Resource.Plastic: 7.5
            },
            'production': {
                Resource.SmartPlating: 5
            }
        },
        'Plutonium Fuel Rod': {
            'consumption': {
                Resource.EncasedPlutoniumCell: 7.5,
                Resource.SteelBeam: 4.5,
                Resource.ElectromagneticControlRod: 1.5,
                Resource.HeatSink: 2.5
            },
            'production': {
                Resource.PlutoniumFuelRod: 0.3
            }
        },
        'Radio Connection Unit': {
            'consumption': {
                Resource.HeatSink: 15,
                Resource.HighSpeedConnector: 7.5,
                Resource.QuartzCrystal: 45
            },
            'production': {
                Resource.RadioControlUnit: 3.8
            }
        },
        'Radio Control System': {
            'consumption': {
                Resource.CrystalOscillator: 1.5,
                Resource.CircuitBoard: 15,
                Resource.AluminumCasing: 90,
                Resource.Rubber: 45
            },
            'production': {
                Resource.RadioControlUnit: 2.5
            }
        },
        'Radio Control Unit': {
            'consumption': {
                Resource.AluminumCasing: 40,
                Resource.CrystalOscillator: 1.25,
                Resource.Computer: 1.25
            },
            'production': {
                Resource.RadioControlUnit: 2.5
            }
        },
        'Rigour Motor': {
            'consumption': {
                Resource.Rotor: 3.75,
                Resource.Stator: 3.75,
                Resource.CrystalOscillator: 1.25
            },
            'production': {
                Resource.Motor: 7.5
            }
        },
        'Silicon High-Speed Connector': {
            'consumption': {
                Resource.Quickwire: 90,
                Resource.Silica: 37.5,
                Resource.CircuitBoard: 3
            },
            'production': {
                Resource.HighSpeedConnector: 3
            }
        },
        'Super-State Computer': {
            'consumption': {
                Resource.Computer: 3.6,
                Resource.ElectromagneticControlRod: 2.4,
                Resource.Battery: 24,
                Resource.Wire: 54
            },
            'production': {
                Resource.Supercomputer: 2.4
            }
        },
        'Supercomputer': {
            'consumption': {
                Resource.Computer: 3.75,
                Resource.AILimiter: 3.75,
                Resource.HighSpeedConnector: 5.625,
                Resource.Plastic: 52.5
            },
            'production': {
                Resource.Supercomputer: 1.9
            }
        },
        'Thermal Propulsion Rocket': {
            'consumption': {
                Resource.ModularEngine: 2.5,
                Resource.TurboMotor: 1,
                Resource.CoolingSystem: 3,
                Resource.FusedModularFrame: 1
            },
            'production': {
                Resource.ThermalPropulsionRocket: 1
            }
        },
        'Turbo Electric Motor': {
            'consumption': {
                Resource.Motor: 6.5625,
                Resource.RadioControlUnit: 8.4375,
                Resource.ElectromagneticControlRod: 4.6875,
                Resource.Rotor: 6.5625
            },
            'production': {
                Resource.TurboMotor: 2.8
            }
        },
        'Turbo Motor': {
            'consumption': {
                Resource.CoolingSystem: 7.5,
                Resource.RadioControlUnit: 3.75,
                Resource.Motor: 7.5,
                Resource.Rubber: 45
            },
            'production': {
                Resource.TurboMotor: 1.9
            }
        },
        'Turbo Pressure Motor': {
            'consumption': {
                Resource.Motor: 7.5,
                Resource.PressureConversionCube: 1.875,
                Resource.PackagedNitrogenGas: 45,
                Resource.Stator: 15
            },
            'production': {
                Resource.TurboMotor: 3.8
            }
        },
        'Turbo Rifle Ammo': {
            'consumption': {
                Resource.RifleAmmo: 125,
                Resource.AluminumCasing: 15,
                Resource.PackagedTurboFuel: 15
            },
            'production': {
                Resource.TurboRifleAmmo: 250
            }
        },
        'Uranium Fuel Rod': {
            'consumption': {
                Resource.EncasedUraniumCell: 20,
                Resource.EncasedIndustrialBeam: 1.2,
                Resource.ElectromagneticControlRod: 2
            },
            'production': {
                Resource.UraniumFuelRod: 0.4
            }
        },

        'Uranium Fuel Unit': {
            'consumption': {
                Resource.EncasedUraniumCell: 20,
                Resource.ElectromagneticControlRod: 2,
                Resource.CrystalOscillator: 0.6,
                Resource.Beacon: 1.2
            },
            'production': {
                Resource.UraniumFuelRod: 0.6
            }
        },
    }


class Packager(Machine):
    recipes = {
        'Packaged Alumina Solution': {
            'consumption': {
                Resource.AluminaSolution: 120,
                Resource.EmptyCanister: 120
            },
            'production': {
                Resource.PackagedAluminaSolution: 120
            }
        },
        'Packaged Fuel': {
            'consumption': {
                Resource.Fuel: 40,
                Resource.EmptyCanister: 40
            },
            'production': {
                Resource.PackagedFuel: 40
            }
        },
        'Packaged Heavy Oil Residue': {
            'consumption': {
                Resource.HeavyOilResidue: 30,
                Resource.EmptyCanister: 30
            },
            'production': {
                Resource.PackagedHeavyOilResidue: 30
            }
        },
        'Packaged Liquid Biofuel': {
            'consumption': {
                Resource.LiquidBiofuel: 40,
                Resource.EmptyCanister: 40
            },
            'production': {
                Resource.PackagedLiquidBiofuel: 40
            }
        },
        'Packaged Nitric Acid': {
            'consumption': {
                Resource.NitricAcid: 30,
                Resource.EmptyFluidTank: 30
            },
            'production': {
                Resource.PackagedNitricAcid: 30
            }
        },
        'Packaged Nitrogen Gas': {
            'consumption': {
                NitrogenGas: 240,
                Resource.EmptyFluidTank: 60
            },
            'production': {
                Resource.PackagedNitrogenGas: 60
            }
        },
        'Packaged Oil': {
            'consumption': {
                CrudeOil: 30,
                Resource.EmptyCanister: 30
            },
            'production': {
                Resource.PackagedOil: 30
            }
        },
        'Packaged Sulfuric Acid': {
            'consumption': {
                Resource.SulfuricAcid: 40,
                Resource.EmptyCanister: 40
            },
            'production': {
                Resource.PackagedSulfuricAcid: 40
            }
        },
        'Packaged Turbofuel': {
            'consumption': {
                Resource.Turbofuel: 20,
                Resource.EmptyCanister: 20
            },
            'production': {
                Resource.PackagedTurboFuel: 20
            }
        },
        'Packaged Water': {
            'consumption': {
                Resource.Water: 60,
                Resource.EmptyCanister: 60
            },
            'production': {
                Resource.PackagedWater: 60
            }
        },
        'Unpackage Alumina Solution': {
            'consumption': {
                Resource.PackagedAluminaSolution: 120
            },
            'production': {
                Resource.AluminaSolution: 120,
                Resource.EmptyCanister: 120
            }
        },
        'Unpackage Fuel': {
            'consumption': {
                Resource.PackagedFuel: 60
            },
            'production': {
                Resource.Fuel: 60,
                Resource.EmptyCanister: 60
            }
        },
        'Unpackage Heavy Oil Residue': {
            'consumption': {
                Resource.PackagedHeavyOilResidue: 20
            },
            'production': {
                Resource.HeavyOilResidue: 20,
                Resource.EmptyCanister: 20
            }
        },
        'Unpackage Liquid Biofuel': {
            'consumption': {
                Resource.PackagedLiquidBiofuel: 60
            },
            'production': {
                Resource.LiquidBiofuel: 60,
                Resource.EmptyCanister: 60
            }
        },
        'Unpackage Nitric Acid': {
            'consumption': {
                Resource.PackagedNitricAcid: 20
            },
            'production': {
                Resource.NitricAcid: 20,
                Resource.EmptyFluidTank: 20
            }
        },
        'Unpackage Nitrogen Gas': {
            'consumption': {
                Resource.PackagedNitrogenGas: 60
            },
            'production': {
                NitrogenGas: 240,
                Resource.EmptyFluidTank: 60
            }
        },
        'Unpackage Oil': {
            'consumption': {
                Resource.PackagedOil: 60
            },
            'production': {
                CrudeOil: 60,
                Resource.EmptyCanister: 60
            }
        },
        'Unpackage Sulfuric Acid': {
            'consumption': {
                Resource.PackagedSulfuricAcid: 60
            },
            'production': {
                Resource.SulfuricAcid: 60,
                Resource.EmptyCanister: 60
            }
        },
        'Unpackage Turbofuel': {
            'consumption': {
                Resource.PackagedTurboFuel: 20
            },
            'production': {
                Resource.Turbofuel: 20,
                Resource.EmptyCanister: 20
            }
        },
        'Unpackage Water': {
            'consumption': {
                Resource.PackagedWater: 120
            },
            'production': {
                Resource.Water: 120,
                Resource.EmptyCanister: 120
            }
        }
    }


class ParticleAccelerator(Machine):
    recipes = {
        'Instant Plutonium Cell': {
            'consumption': {
                Resource.NonFissileUranium: 75,
                Resource.AluminumCasing: 10
            },
            'production': {
                Resource.EncasedPlutoniumCell: 10
            }
        },
        'Nuclear Pasta': {
            'consumption': {
                Resource.CopperPowder: 100,
                Resource.PressureConversionCube: 0.5
            },
            'production': {
                Resource.NuclearPasta: 0.5
            }
        },
        'Plutonium Pellet': {
            'consumption': {
                Resource.NonFissileUranium: 100,
                Resource.UraniumWaste: 25
            },
            'production': {
                Resource.PlutoniumPellet: 30
            }
        }
    }


class Refinery(Machine):
    recipes = {
        'Alumina Solution': {
            'consumption': {
                Bauxite: 120,
                Resource.Water: 180
            },
            'production': {
                Resource.AluminaSolution: 120,
                Resource.Silica: 50
            }
        },
        'Aluminum Scrap': {
            'consumption': {
                Resource.AluminaSolution: 240,
                Coal: 120
            },
            'production': {
                Resource.AluminumScrap: 360,
                Resource.Water: 120
            }
        },
        'Coated Cable': {
            'consumption': {
                Resource.Wire: 37.5,
                Resource.HeavyOilResidue: 15
            },
            'production': {
                Resource.Cable: 67.5
            }
        },
        'Diluted Packaged Fuel': {
            'consumption': {
                Resource.HeavyOilResidue: 30,
                Resource.PackagedWater: 60
            },
            'production': {
                Resource.PackagedFuel: 60
            }
        },
        'Electrode-Aluminum Scrap': {
            'consumption': {
                Resource.AluminaSolution: 180,
                Resource.PetroleumCoke: 60
            },
            'production': {
                Resource.AluminumScrap: 300,
                Resource.Water: 105
            }
        },
        'Fuel': {
            'consumption': {
                CrudeOil: 60
            },
            'production': {
                Resource.Fuel: 40,
                Resource.PolymerResin: 30
            }
        },
        'Heavy Oil Residue': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                Resource.HeavyOilResidue: 40,
                Resource.PolymerResin: 20
            }
        },
        'Liquid Biofuel': {
            'consumption': {
                Resource.SolidBiofuel: 990,
                Resource.Water: 45
            },
            'production': {
                Resource.LiquidBiofuel: 60
            }
        },
        'Petroleum Coke': {
            'consumption': {
                Resource.HeavyOilResidue: 40
            },
            'production': {
                Resource.PetroleumCoke: 120
            }
        },
        'Plastic': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                Resource.Plastic: 20,
                Resource.HeavyOilResidue: 10
            }
        },
        'Polyester Fabric': {
            'consumption': {
                Resource.PolymerResin: 30,
                Resource.Water: 30
            },
            'production': {
                Resource.Fabric: 30
            }
        },
        'Polymer Resin': {
            'consumption': {
                CrudeOil: 60
            },
            'production': {
                Resource.PolymerResin: 130,
                Resource.HeavyOilResidue: 20
            }
        },
        'Pure Caterium Ingot': {
            'consumption': {
                CateriumOre: 24,
                Resource.Water: 24
            },
            'production': {
                Resource.CateriumIngot: 12
            }
        },
        'Pure Copper Ingot': {
            'consumption': {
                CopperOre: 15,
                Resource.Water: 10
            },
            'production': {
                Resource.CopperIngot: 37.5
            }
        },
        'Pure Iron Ingot': {
            'consumption': {
                IronOre: 35,
                Resource.Water: 20
            },
            'production': {
                Resource.IronIngot: 65
            }
        },
        'Pure Quartz Crystal': {
            'consumption': {
                RawQuartz: 67.5,
                Resource.Water: 37.5
            },
            'production': {
                Resource.QuartzCrystal: 52.5
            }
        },
        'Recycled Plastic': {
            'consumption': {
                Resource.Rubber: 30,
                Resource.Fuel: 30
            },
            'production': {
                Resource.Plastic: 60
            }
        },
        'Recycled Rubber': {
            'consumption': {
                Resource.Plastic: 30,
                Resource.Fuel: 30
            },
            'production': {
                Resource.Rubber: 60
            }
        },
        'Residual Fuel': {
            'consumption': {
                Resource.HeavyOilResidue: 60
            },
            'production': {
                Resource.Fuel: 40
            }
        },
        'Residual Plastic': {
            'consumption': {
                Resource.PolymerResin: 60,
                Resource.Water: 20
            },
            'production': {
                Resource.Plastic: 20
            }
        },
        'Residual Rubber': {
            'consumption': {
                Resource.PolymerResin: 40,
                Resource.Water: 40
            },
            'production': {
                Resource.Rubber: 20
            }
        },
        'Rubber': {
            'consumption': {
                CrudeOil: 30
            },
            'production': {
                Resource.Rubber: 20,
                Resource.HeavyOilResidue: 20
            }
        },
        'Sloppy Alumina': {
            'consumption': {
                Bauxite: 200,
                Resource.Water: 200
            },
            'production': {
                Resource.AluminaSolution: 240
            }
        },
        'Smokeless Powder': {
            'consumption': {
                Resource.BlackPowder: 20,
                Resource.HeavyOilResidue: 10
            },
            'production': {
                Resource.SmokelessPowder: 20
            }
        },
        'Steamed Copper Sheet': {
            'consumption': {
                Resource.CopperIngot: 22.5,
                Resource.Water: 22.5
            },
            'production': {
                Resource.CopperSheet: 22.5
            }
        },
        'Sulfuric Acid': {
            'consumption': {
                Sulfur: 50,
                Resource.Water: 50
            },
            'production': {
                Resource.SulfuricAcid: 50
            }
        },
        'Turbo Heavy Fuel': {
            'consumption': {
                Resource.HeavyOilResidue: 37.5,
                Resource.CompactedCoal: 30
            },
            'production': {
                Resource.Turbofuel: 30
            }
        },
        'TurboFuel': {
            'consumption': {
                Resource.Fuel: 22.5,
                Resource.CompactedCoal: 15
            },
            'production': {
                Resource.Turbofuel: 18.8
            }
        },
        'Wet Concrete': {
            'consumption': {
                Limestone: 120,
                Resource.Water: 100
            },
            'production': {
                Resource.Concrete: 80
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
                Resource.CateriumIngot: 15
            }
        },
        'Copper Ingot': {
            'consumption': {
                CopperOre: 30
            },
            'production': {
                Resource.CopperIngot: 30
            }
        },
        'Iron Ingot': {
            'consumption': {
                IronOre: 30
            },
            'production': {
                Resource.IronIngot: 30
            }
        },
        'Pure Aluminum Ingot': {
            'consumption': {
                Resource.AluminumScrap: 30
            },
            'production': {
                Resource.AluminumIngot: 30
            }
        }
    }
