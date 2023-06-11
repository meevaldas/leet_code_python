import unittest
from search_in_rotated_sorted_array import Solution


class TestSearchInRotSortArray(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().search([1], 0), -1)
