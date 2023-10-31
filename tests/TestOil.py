import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Resource.Oil import Oil


class TestOil(unittest.TestCase):
    def test_get_name(self):
        """
        Oil.get_name() return the class name.
        :return:
        """
        oil = Oil('Impure')
        self.assertEqual(oil.get_name(), 'Oil')

    def test_get_sinkable(self):
        """
        Oil.get_sinkable() returns False because liquids are not sinkable
        :return:
        """
        oil = Oil('Impure')
        self.assertEqual(oil.get_sinkable(), False)

    def test_get_class(self):
        """
        Oil.get_class() returns a reference to its own class
        :return:
        """
        oil = Oil('Impure')
        self.assertEqual(oil.get_class(), Oil)

    def test_purity(self):
        """
        Oil.get_purity() returns a purity modifier to modify a Miners mine rate based on
        the purity of the ore node
        :return:
        """
        oil = Oil('Impure')
        self.assertEqual(oil.get_purity_modifier(), 1)

        oil = Oil('Normal')
        self.assertEqual(oil.get_purity_modifier(), 2)

        oil = Oil('Pure')
        self.assertEqual(oil.get_purity_modifier(), 4)

        with self.assertRaises(KeyError):
            oil = Oil('Invalid Input')


if __name__ == '__main__':
    unittest.main()
