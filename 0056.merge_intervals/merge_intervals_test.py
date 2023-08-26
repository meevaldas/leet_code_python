import unittest
from merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])

    def test_example_two(self):
        self.assertEqual(Solution().merge([[1, 4], [4, 5]]), [[1, 5]])
