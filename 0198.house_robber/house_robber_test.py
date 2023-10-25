import unittest
from house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)

    def test_example_two(self):
        self.assertEqual(Solution().rob([2, 7, 9, 3, 1]), 12)
