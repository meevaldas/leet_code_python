import unittest
from search_a_2d_matrix import Solution


class TestSearch2DMatrix(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False)
