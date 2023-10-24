import unittest
from best_time_to_sell_the_stock import Solution


class TestBestTimeToSell(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().max_profit([7, 6, 4, 3, 1]), 0)
