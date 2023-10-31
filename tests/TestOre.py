import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Resource.Ore import Ore


class TestOre(unittest.TestCase):
    def test_get_name(self):
        """
        Ore.get_name() return the class name.
        :return:
        """
        ore = Ore('Impure')
        self.assertEqual(ore.get_name(), 'Ore')

    def test_get_sinkable(self):
        """
        Ore.get_sinkable() returns True by default
        :return:
        """
        ore = Ore('Impure')
        self.assertEqual(ore.get_sinkable(), True)

    def test_get_class(self):
        """
        Ore.get_class() returns a reference to its own class
        :return:
        """
        ore = Ore('Impure')
        self.assertEqual(ore.get_class(), Ore)

    def test_purity(self):
        """
        Ore.get_purity() returns a purity modifier to modify a Miners mine rate based on
        the purity of the ore node
        :return:
        """
        ore = Ore('Impure')
        self.assertEqual(ore.get_purity_modifier(), 1)

        ore = Ore('Normal')
        self.assertEqual(ore.get_purity_modifier(), 2)

        ore = Ore('Pure')
        self.assertEqual(ore.get_purity_modifier(), 4)

        with self.assertRaises(KeyError):
            ore = Ore('Invalid Input')


if __name__ == '__main__':
    unittest.main()
