import unittest
from find_min_in_rot_sorted_array import Solution


class TestFindMinimumInSortedArray(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().find_min([3, 4, 5, 1, 2]), 1)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().find_min([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().find_min([11, 13, 15, 17]), 11)
