import unittest
from container_with_most_water import Solution


class TestMostWaterContainer(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().max_area([1, 1]), 1)
