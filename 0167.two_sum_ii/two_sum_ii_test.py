import unittest
from two_sum_ii import Solution


class TestTwoSumII(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().two_sum([2, 3, 4], 6), [1, 3])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().two_sum([-1, 0], -1), [1, 2])
