import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Machines.Machines import Machine, FuelGenerator
from SatisfactoryPlanner.Resource.Ore import IronOre
from SatisfactoryPlanner.Resource.Resource import IronIngot


class TestMachine(unittest.TestCase):
    def test_clock_speed(self):
        test_recipe = 'Example Recipe'
        base_recipe = Machine.recipes[test_recipe]

        # Normal
        modifier = 1.00
        machine = Machine(test_recipe, clock_speed_modifier=modifier)
        self.assertEqual(machine.get_consumption_rates()[IronOre], base_recipe['consumption'][IronOre] * modifier)
        self.assertEqual(machine.get_production_rates()[IronIngot], base_recipe['production'][IronIngot] * modifier)

        # Max
        modifier = 2.50
        machine = Machine(test_recipe, clock_speed_modifier=modifier)
        self.assertEqual(machine.get_consumption_rates()[IronOre], base_recipe['consumption'][IronOre] * modifier)
        self.assertEqual(machine.get_production_rates()[IronIngot], base_recipe['production'][IronIngot] * modifier)

        # Min
        modifier = 0.25
        machine = Machine(test_recipe, clock_speed_modifier=modifier)
        self.assertEqual(machine.get_consumption_rates()[IronOre], base_recipe['consumption'][IronOre] * modifier)
        self.assertEqual(machine.get_production_rates()[IronIngot], base_recipe['production'][IronIngot] * modifier)

        # Test bounds (upper)
        with self.assertRaises(ValueError):
            machine = Machine(test_recipe, clock_speed_modifier=2.51)

            # Test bounds (lower)
            with self.assertRaises(ValueError):
                machine = Machine(test_recipe, clock_speed_modifier=0.24)

    def test_allow_undersupply(self):
        """
        Normal machines don't allow underflow by default. The exception is fuel generators, which
        is an option that can be specified at initialization.

        Factories use undersupply information to determine if they are consuming/producing the correct
        amount of resources.
        :return:
        """
        test_recipe = 'Example Recipe'

        modifier = 1.00
        machine = Machine(test_recipe, clock_speed_modifier=modifier)
        self.assertEqual(machine.get_allow_undersupply(), False)

        machine = FuelGenerator('Fuel', clock_speed_modifier=1, allow_undersupply=False)
        self.assertEqual(machine.get_allow_undersupply(), False)

        machine = FuelGenerator('Fuel', clock_speed_modifier=1, allow_undersupply=True)
        self.assertEqual(machine.get_allow_undersupply(), True)


if __name__ == '__main__':
    unittest.main()
