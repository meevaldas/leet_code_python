import unittest
from operator import itemgetter
from typing import List
from group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_example_one(self):
        sorted_solution = sorted([sorted(inner_list) for inner_list in Solution().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])])
        sorted_expected = sorted([sorted(inner_list) for inner_list in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
        self.assertListEqual(sorted_solution, sorted_expected)
    def test_example_two(self):
        sorted_solution = sorted([sorted(inner_list) for inner_list in Solution().group_anagrams([""])])
        sorted_expected = sorted([sorted(inner_list) for inner_list in [[""]]])
        self.assertListEqual(sorted_solution, sorted_expected)

    def test_example_three(self):
        sorted_solution = sorted([sorted(inner_list) for inner_list in Solution().group_anagrams(["a"])])
        sorted_expected = sorted([sorted(inner_list) for inner_list in [["a"]]])
        self.assertListEqual(sorted_solution, sorted_expected)



