import unittest
from car_fleet import Solution


class TestCarFleet(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().car_fleet(10, [3], [3]), 1)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().car_fleet(100, [0, 2, 4], [4, 2, 1]), 1)
