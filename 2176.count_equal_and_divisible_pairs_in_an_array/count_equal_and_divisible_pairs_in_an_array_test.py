import unittest
from count_equal_and_divisible_pairs_in_an_array import Solution


class TestCountEqualAndDivisiblePairs(unittest.TestCase):
    def test_count_equal_and_divisible_pairs_one(self):
        self.assertAlmostEqual(Solution().count_pairs([3, 1, 2, 2, 2, 1, 3], 2), 4)

    def test_count_equal_and_divisible_pairs_two(self):
        self.assertAlmostEqual(Solution().count_pairs([1, 2, 3, 4], 1), 0)
