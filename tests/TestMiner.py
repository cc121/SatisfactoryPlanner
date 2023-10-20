import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner
from SatisfactoryPlanner.Resource.Resource import IronOre


class TestMiner(unittest.TestCase):
    def test_mark1_impure(self):
        miner = Miner(1, IronOre('Impure'))
        self.assertEqual(miner.get_capacity()[IronOre], 30)

    def test_mark2_impure(self):
        miner = Miner(2, IronOre('Impure'))
        self.assertEqual(miner.get_capacity()[IronOre], 60)

    def test_mark3_impure(self):
        miner = Miner(3, IronOre('Impure'))
        self.assertEqual(miner.get_capacity()[IronOre], 120)

    def test_mark1_normal(self):
        miner = Miner(1, IronOre('Normal'))
        self.assertEqual(miner.get_capacity()[IronOre], 60)

    def test_mark2_normal(self):
        miner = Miner(2, IronOre('Normal'))
        self.assertEqual(miner.get_capacity()[IronOre], 120)

    def test_mark3_normal(self):
        miner = Miner(3, IronOre('Normal'))
        self.assertEqual(miner.get_capacity()[IronOre], 240)

    def test_mark1_pure(self):
        miner = Miner(1, IronOre('Pure'))
        self.assertEqual(miner.get_capacity()[IronOre], 120)

    def test_mark2_pure(self):
        miner = Miner(2, IronOre('Pure'))
        self.assertEqual(miner.get_capacity()[IronOre], 240)

    def test_mark3_pure(self):
        miner = Miner(3, IronOre('Pure'))
        self.assertEqual(miner.get_capacity()[IronOre], 480)


if __name__ == '__main__':
    unittest.main()
