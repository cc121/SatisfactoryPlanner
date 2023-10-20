import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner, Factory
from SatisfactoryPlanner.Resource.Resource import IronOre, IronRod
from SatisfactoryPlanner.Machines.Machines import Smelter, Constructor


class TestFactory(unittest.TestCase):
    def test_single_simple_factory(self):
        miner = Miner(1, IronOre('Impure'))
        factory = Factory()

        # Add 30 Iron/minute capacity to the current factory
        factory.add_input(miner)

        # Produce Iron Ingots using a Smelter
        factory.add_machine(Smelter('Iron Ingot'))

        # Confirm Iron Ingots are being produced
        self.assertEqual(factory.get_capacity(), Smelter('Iron Ingot').get_production_rates())

    def test_assembler_factory(self):
        raise NotImplementedError("Implement me!")

    def test_blender_factory(self):
        raise NotImplementedError("Implement me!")

    def test_constructor_factory(self):
        miner = Miner(1, IronOre('Impure'))
        factory = Factory()

        # Add 30 Iron/minute capacity to the current factory
        factory.add_input(miner)

        # Produce Iron Ingots using a Smelter
        factory.add_machine(Smelter('Iron Ingot'))

        # Produce Iron Rods up to maximum available
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Iron Rod'))

        # Confirm Iron Rods are being produced
        self.assertEqual(factory.get_capacity()[IronRod], Constructor('Iron Rod').get_production_rates()[IronRod]*2)

    def test_constructor_factory_overconsumption(self):
        miner = Miner(1, IronOre('Impure'))
        factory = Factory()

        # Add 30 Iron/minute capacity to the current factory
        factory.add_input(miner)

        # Produce Iron Ingots using a Smelter
        factory.add_machine(Smelter('Iron Ingot'))

        # Product Iron Rods beyond available Iron Ingots
        factory.add_machine(Constructor('Iron Rod'))
        factory.add_machine(Constructor('Iron Rod'))

        # Confirm that we fail to add the new constructor, exceeding capacity
        with self.assertRaises(ValueError):
            factory.add_machine(Constructor('Iron Rod'))

    def test_foundry_factory(self):
        raise NotImplementedError("Implement me!")

    def test_manufacturer_factory(self):
        raise NotImplementedError("Implement me!")

    def test_oil_extractor_factory(self):
        raise NotImplementedError("Implement me!")

    def test_packager_factory(self):
        raise NotImplementedError("Implement me!")

    def test_particle_accelerator_factory(self):
        raise NotImplementedError("Implement me!")

    def test_refinery_factory(self):
        raise NotImplementedError("Implement me!")

    def test_smelter_factory(self):
        raise NotImplementedError("Implement me!")

    def test_water_extractor_factory(self):
        raise NotImplementedError("Implement me!")


if __name__ == '__main__':
    unittest.main()
