import unittest
from valid_anagrams import Solution


class TestAnagrams(unittest.TestCase):
    def test_anagram_example_one(self):
        self.assertAlmostEqual(Solution().is_anagram("anagram", "nagaram"), True)

    def test_anagram_example_two(self):
        self.assertAlmostEqual(Solution().is_anagram("rat", "car"), False)
