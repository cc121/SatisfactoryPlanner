import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory
from SatisfactoryPlanner.Resource.Resource import *
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor, Assembler


class TestSpaceElevator(unittest.TestCase):
    def test_tier_1(self):
        factory = Factory()

        # Reinforced Iron Plate tree
        ## Build plates
        factory.add_input(Miner(1, IronOre('Impure')))
        factory.add_input(Miner(1, IronOre('Impure')))
        factory.add_machine(Smelter('Iron Ingot'))
        factory.add_machine(Smelter('Iron Ingot'))
        factory.add_machine(Constructor('Iron Plate'))
        factory.add_machine(Constructor('Iron Plate'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronPlate: 40})

        ## Build screws
        factory.add_input(Miner(1, IronOre('Impure')))
        factory.add_machine(Smelter('Iron Ingot'))
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Screw'))
        factory.add_machine(Constructor('Screw'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronRod: 10, IronPlate: 40, Screw: 80})

        # Build plates
        factory.add_machine(Assembler('Reinforced Iron Plate'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronRod: 10, IronPlate: 10, Screw: 20, ReinforcedIronPlate:5})

        # Rotor tree
        # Build screws and iron rods (we have an excess of 20/min screws from Reinforced Iron Plate tree
        factory.add_input(Miner(1, IronOre('Impure')))
        factory.add_machine(Smelter('Iron Ingot'))
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Screw'))
        factory.add_machine(Constructor('Screw'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronRod: 20, IronPlate: 10, Screw: 100, ReinforcedIronPlate: 5})

        # Tree 2
        factory.add_machine(Assembler('Rotor'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronRod: 0, IronPlate: 10, Screw: 0, ReinforcedIronPlate: 5, Rotor: 4})

        # Produce the Smart Plating at 2/minute
        factory.add_machine(Assembler('Smart Plating'))

        self.assertEqual(factory.get_capacity(), {IronIngot: 0, IronRod: 0, IronPlate: 10, Screw: 0, ReinforcedIronPlate: 3, Rotor: 2, SmartPlating: 2})


if __name__ == '__main__':
    unittest.main()
