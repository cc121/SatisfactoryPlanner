import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory
from SatisfactoryPlanner.Resource.Resource import IronRod, IronIngot, Screw
from SatisfactoryPlanner.Resource.Ore import IronOre
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor


class TestFactory(unittest.TestCase):
    def test_basic_functionality(self):
        factory = Factory('Test Factory')

        miner = Miner(1, IronOre('Impure'))
        factory.add_input(miner)

        # Confirm correct production (intermediate)
        self.assertEqual(miner.get_capacity(), {IronOre: 30})

        factory.add_machine(Smelter('Iron Ingot'))

        # Confirm correct production
        self.assertEqual(factory.get_capacity(), Smelter('Iron Ingot').get_production_rates())

        # Confirm correct consumption
        self.assertEqual(miner.get_capacity(), {IronOre: 0})

    def test_advanced_functionality(self):
        factory = Factory('Test Factory')

        # Build and test inputs and internal production for screw production
        miner = Miner(1, IronOre('Impure'))
        factory.add_input(miner)

        # Confirm correct production (intermediate)
        factory.add_machine(Smelter('Iron Ingot'))
        self.assertEqual(factory.get_capacity(), {IronIngot: 30})

        # Confirm correct production (intermediate)
        factory.add_machine(Constructor('Iron Rod'))
        self.assertEqual(factory.get_capacity(), {IronIngot: 15, IronRod: 15})

        factory.add_machine(Constructor('Screw'))

        # Confirm correct production
        self.assertEqual(factory.get_capacity(), {IronIngot: 15, IronRod: 5, Screw: 40})

    def test_input_miner_upgrade(self):
        factory = Factory('Test Factory')

        miner = Miner(1, IronOre('Impure'))
        factory.add_input(miner)

        # Confirm correct production (intermediate)
        self.assertEqual(miner.get_capacity(), {IronOre: 30})

        factory.upgrade_miners(2)

        # Confirm correct production
        self.assertEqual(miner.get_capacity(), {IronOre: 60})

    def test_get_name(self):
        factory = Factory('Test Factory')

        self.assertEqual(factory.get_name(), 'Test Factory')

    def test_get_inputs(self):
        factory = Factory('Test Factory')

        miner = Miner(1, IronOre('Impure'))
        factory.add_input(miner)

        self.assertEqual(factory.get_inputs(), [miner])


if __name__ == '__main__':
    unittest.main()
