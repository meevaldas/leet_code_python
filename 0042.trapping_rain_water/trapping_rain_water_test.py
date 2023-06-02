import unittest
from trapping_rain_water import Solution


class TestTrappingRainWater(unittest.TestCase):
    def test_trap_example_one(self):
        self.assertAlmostEqual(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_trap_example_two(self):
        self.assertAlmostEqual(Solution().trap([4, 2, 0, 3, 2, 5]), 9)
