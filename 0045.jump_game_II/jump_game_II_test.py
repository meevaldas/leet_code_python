import unittest
from jump_game_II import Solution


class TestJumpGameII(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().jump([2, 3, 1, 1, 4]), 2)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().jump([2, 3, 0, 1, 4]), 2)
