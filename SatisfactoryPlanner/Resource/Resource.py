class Resource:
    NAME=None

    def __init__(self, purity):
        purity_modifier_table = {
            "Impure": 1,
            "Normal": 2,
            "Pure": 4
        }
        self.purity_modifier = purity_modifier_table[purity]

    def get_name(self):
        return self.__class__.__name__

    def get_purity_modifier(self) -> int:
        return self.purity_modifier


class Bauxite(Resource):
    pass


class Caterium(Resource):
    pass


class Coal(Resource):
    pass


class Copper(Resource):
    pass


class Iron(Resource):
    pass


class Limestone(Resource):
    pass


class Quartz(Resource):
    pass


class SAM(Resource):
    pass


class Sulfur(Resource):
    pass


class Uranium(Resource):
    pass
