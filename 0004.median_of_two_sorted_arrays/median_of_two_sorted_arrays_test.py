import unittest
from median_of_two_sorted_arrays import Solution


class TestMedianSortedArrays(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().find_median_sorted_arrays([1, 3], [2]), 2.00000)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().find_median_sorted_arrays([1, 2], [3, 4]), 2.50000)
