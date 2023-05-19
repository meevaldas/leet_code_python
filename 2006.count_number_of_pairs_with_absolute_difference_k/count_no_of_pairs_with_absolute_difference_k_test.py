import unittest
from count_no_of_pairs_with_absolute_difference_k import Solution


class TestCountNoOfPairsWithAbsoluteDifferenceK(unittest.TestCase):
    def test_count_no_of_pairs_example_one(self):
        self.assertAlmostEqual(Solution().count_k_difference([1, 2, 2, 1], 1), 4)

    def test_count_no_of_pairs_example_two(self):
        self.assertAlmostEqual(Solution().count_k_difference([1, 3], 3), 0)

    def test_count_no_of_pairs_example_three(self):
        self.assertAlmostEqual(Solution().count_k_difference([3, 2, 1, 5, 4], 2), 3)
