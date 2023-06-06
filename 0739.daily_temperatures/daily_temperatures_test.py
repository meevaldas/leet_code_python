import unittest
from daily_temperatures import Solution


class TestDailyTemperature(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().daily_temperatures([30, 60, 90]), [1, 1, 0])
