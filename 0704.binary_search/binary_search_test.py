import unittest
from binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().search([-1, 0, 3, 5, 9, 12], 2), -1)
