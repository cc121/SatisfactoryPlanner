class Resource:
    @classmethod
    def get_name(cls):
        return cls.__name__

    def get_class(self):
        return self.__class__


class AlienDNACapsule(Resource):
    pass


class AlienProtein(Resource):
    pass


class AluminumCasing(Resource):
    pass


class AluminumIngot(Resource):
    pass


class AluminumScrap(Resource):
    pass


class Biomass(Resource):
    pass


class BluePowerSlug(Resource):
    pass


class Cable(Resource):
    pass


class CateriumIngot(Resource):
    pass


class ColorCartridge(Resource):
    pass


class Concrete(Resource):
    pass

class CopperIngot(Resource):
    pass


class CopperPowder(Resource):
    pass


class CopperSheet(Resource):
    pass


class EmptyCanister(Resource):
    pass


class EmptyFluidTank(Resource):
    pass


class FlowerPetals(Resource):
    pass


class HatcherRemains(Resource):
    pass


class HogRemains(Resource):
    pass


class IronIngot(Resource):
    pass


class IronPlate(Resource):
    pass


class IronRebar(Resource):
    pass


class IronRod(Resource):
    pass


class Leaves(Resource):
    pass


class Mycelia(Resource):
    pass


class PlasmaSpitterRemains(Resource):
    pass


class Plastic(Resource):
    pass


class PowerShard(Resource):
    pass


class PurplePowerSlug(Resource):
    pass


class QuartzCrystal(Resource):
    pass


class Quickwire(Resource):
    pass


class Screw(Resource):
    pass


class Silica(Resource):
    pass


class SolidBiofuel(Resource):
    pass


class SteelBeam(Resource):
    pass


class SteelIngot(Resource):
    pass


class SteelPipe(Resource):
    pass


class StingerRemains(Resource):
    pass


class Wire(Resource):
    pass


class Wood(Resource):
    pass


class YellowPowerSlug(Resource):
    pass


class Ore(Resource):
    def __init__(self, purity):
        purity_modifier_table = {
            "Impure": 1,
            "Normal": 2,
            "Pure": 4
        }
        self.purity_modifier = purity_modifier_table[purity]

    def get_purity_modifier(self) -> int:
        return self.purity_modifier


class Bauxite(Ore):
    pass


class CateriumOre(Ore):
    pass


class Coal(Ore):
    pass


class CopperOre(Ore):
    pass


class IronOre(Ore):
    pass


class Limestone(Ore):
    pass


class RawQuartz(Ore):
    pass


class SAM(Ore):
    pass


class Sulfur(Ore):
    pass


class Uranium(Ore):
    pass
