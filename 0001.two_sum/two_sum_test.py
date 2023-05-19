import unittest
from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum_example_one(self):
        self.assertAlmostEqual(Solution().two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_example_two(self):
        self.assertAlmostEqual(Solution().two_sum([3, 2, 4], 6), [1, 2])

    def test_two_sum_example_three(self):
        self.assertAlmostEqual(Solution().two_sum([3, 3], 6), [0, 1])
