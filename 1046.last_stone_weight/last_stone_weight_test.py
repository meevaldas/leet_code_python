import unittest
from last_stone_weight import Solution


class TestLastStoneWeight(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().last_stone_weight([2,7,4,1,8,1]), 1)

    def test_example_two(self):
        self.assertEqual(Solution().last_stone_weight([1]), 1)
