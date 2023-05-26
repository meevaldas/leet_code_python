import unittest
from longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_long_consecutive_sequence_example_one(self):
        self.assertAlmostEqual(Solution().longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_long_consecutive_sequence_example_two(self):
        self.assertAlmostEqual(Solution().longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
