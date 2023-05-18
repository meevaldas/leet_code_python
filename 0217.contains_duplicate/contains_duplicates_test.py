"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

import unittest
from contains_duplicates import Solution


class TestDuplicates(unittest.TestCase):

    def test_duplicates_example_one(self):
        self.assertAlmostEqual(Solution().contains_duplicate([1, 2, 3, 1]), True)

    def test_duplicates_example_two(self):
        self.assertAlmostEqual((Solution().contains_duplicate([1, 2, 3, 4])), False)

    def test_duplicates_example_three(self):
        self.assertAlmostEqual(Solution().contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
