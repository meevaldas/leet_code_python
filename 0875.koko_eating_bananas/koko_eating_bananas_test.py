import unittest
from koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().min_eating_speed([30, 11, 23, 4, 20], 5), 30)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().min_eating_speed([30, 11, 23, 4, 20], 6), 23)
