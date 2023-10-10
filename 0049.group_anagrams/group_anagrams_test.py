import unittest
from operator import itemgetter
from typing import List
from group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_example_one(self):
        self.assertCountEqual(Solution().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    # def sort_list_of_list(self, list_of_list: List[List[str]]):
    #     for lst in list_of_list:
    #         lst.sort()
    #
    #     list_of_list.sort(key=itemgetter(0))
    #     return list_of_list
    #
    # def test_one(self):
    #     self.assertListEqual(
    #         self.sort_list_of_list(Solution().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
    #         self.sort_list_of_list([["bat"], ["nat", "tan"], ["eat", "tea", "ate"]]))
    #
    # def test_group_anagrams_example_two(self):
    #     self.assertListEqual(self.sort_list_of_list(Solution().group_anagrams([""])), self.sort_list_of_list([[""]]))
    #
    # def test_group_anagrams_example_three(self):
    #     self.assertListEqual(self.sort_list_of_list(Solution().group_anagrams(["a"])), self.sort_list_of_list([["a"]]))


