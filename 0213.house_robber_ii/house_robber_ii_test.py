import unittest
from house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().rob([2, 3, 2]), 3)

    def test_example_two(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)
