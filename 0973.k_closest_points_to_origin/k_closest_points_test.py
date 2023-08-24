import unittest
from k_closest_points import Solution


class TestKClosest(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])

    def test_example_two(self):
        self.assertEqual(Solution().k_closest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
