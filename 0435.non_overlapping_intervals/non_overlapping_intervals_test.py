import unittest
from non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_example_two(self):
        self.assertEqual(Solution().erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)
