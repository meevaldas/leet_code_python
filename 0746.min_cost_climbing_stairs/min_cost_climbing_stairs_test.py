import unittest
from min_cost_climbing_stairs import Solution


class TestMinCost(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().min_cost_climbing_stairs([10, 15, 20]), 15)

    def test_example_two(self):
        self.assertEqual(Solution().min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
