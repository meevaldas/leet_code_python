import unittest
from jump_game import Solution


class TestJumpGame(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().can_jump([2, 3, 1, 1, 4]), True)

    def test_example_two(self):
        self.assertEqual(Solution().can_jump([3, 2, 1, 0, 4]), False)
