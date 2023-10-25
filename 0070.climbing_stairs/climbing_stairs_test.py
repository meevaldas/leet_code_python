import unittest
from climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().climb_stairs(2), 2)

    def test_example_two(self):
        self.assertEqual(Solution().climb_stairs(3), 3)
