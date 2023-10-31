from SatisfactoryPlanner.Resource.Resource import Resource


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
    SINKABLE = False


class Sulfur(Ore):
    pass


class Uranium(Ore):
    pass
