import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Factory.Factory import Miner
from SatisfactoryPlanner.Resource.Resource import Iron


class TestMiner(unittest.TestCase):
    def test_mark1_impure(self):
        miner = Miner(1, Iron('Impure'))
        self.assertEqual(miner.get_capacity()['Iron'], 30)

    def test_mark2_impure(self):
        miner = Miner(2, Iron('Impure'))
        self.assertEqual(miner.get_capacity()['Iron'], 60)

    def test_mark3_impure(self):
        miner = Miner(3, Iron('Impure'))
        self.assertEqual(miner.get_capacity()['Iron'], 120)

    def test_mark1_normal(self):
        miner = Miner(1, Iron('Normal'))
        self.assertEqual(miner.get_capacity()['Iron'], 60)

    def test_mark2_normal(self):
        miner = Miner(2, Iron('Normal'))
        self.assertEqual(miner.get_capacity()['Iron'], 120)

    def test_mark3_normal(self):
        miner = Miner(3, Iron('Normal'))
        self.assertEqual(miner.get_capacity()['Iron'], 240)

    def test_mark1_pure(self):
        miner = Miner(1, Iron('Pure'))
        self.assertEqual(miner.get_capacity()['Iron'], 120)

    def test_mark2_pure(self):
        miner = Miner(2, Iron('Pure'))
        self.assertEqual(miner.get_capacity()['Iron'], 240)

    def test_mark3_pure(self):
        miner = Miner(3, Iron('Pure'))
        self.assertEqual(miner.get_capacity()['Iron'], 480)


if __name__ == '__main__':
    unittest.main()
