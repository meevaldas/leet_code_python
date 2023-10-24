import unittest
from longest_substring import Solution


class TestLongestSubstring(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().length_of_longest_substring("abcabcbb"), 3)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().length_of_longest_substring("bbbbb"), 1)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().length_of_longest_substring("pwwkew"), 3)
