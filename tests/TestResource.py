import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SatisfactoryPlanner.Resource.Resource import Resource


class TestResource(unittest.TestCase):
    def test_get_name(self):
        """
        Resource.get_name() return the class name.
        :return:
        """
        resource = Resource()
        self.assertEqual(resource.get_name(), 'Resource')

    def test_get_sinkable(self):
        """
        Resource.get_sinkable() returns True by default
        :return:
        """
        resource = Resource()
        self.assertEqual(resource.get_sinkable(), True)

    def test_get_class(self):
        """
        Resource.get_class() returns a reference to its own class
        :return:
        """
        resource = Resource()
        self.assertEqual(resource.get_class(), Resource)

if __name__ == '__main__':
    unittest.main()
