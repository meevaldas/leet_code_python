import unittest
from combination_sum import Solution


class TestCombinationSum(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().combination_sum([2], 1), [])
