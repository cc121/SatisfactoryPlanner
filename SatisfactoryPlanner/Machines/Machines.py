from ..Resource.Resource import *


class Machine:
    def __init__(self, recipe_name):
        self.consumption_rates = self.recipes[recipe_name]["consumption"]
        self.production_rates = self.recipes[recipe_name]["production"]

    def get_consumption_rate(self):
        return self.consumption_rates

    def get_production_rates(self):
        return self.production_rates


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
