import unittest
from group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams_example_one(self):
        self.assertAlmostEqual(Solution().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                               [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    def test_group_anagrams_example_two(self):
        self.assertAlmostEqual(Solution().group_anagrams([""]), [[""]])

    def test_group_anagrams_example_three(self):
        self.assertAlmostEqual(Solution().group_anagrams(["a"]), [["a"]])
