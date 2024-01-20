import unittest
from happy_number import Solution


class TestHappyNumber(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().is_happy(19), True)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().is_happy(2), False)