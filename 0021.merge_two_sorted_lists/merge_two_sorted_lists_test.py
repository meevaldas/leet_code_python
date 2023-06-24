import unittest
from merge_two_sorted_lists import Solution


class TestMergeSortedArrays(unittest.TestCase):
    def _test_example_one(self):
        self.assertAlmostEqual(Solution().merge_two_lists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().merge_two_lists([], []), [])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().merge_two_lists([], [0]), [0])
