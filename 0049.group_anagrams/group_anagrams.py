"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # If word is not in dictionary
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [word]
            # If previously it is present that means its anagram
            # was previously present
            else:
                dictionary[sorted_word] += [word]
        return [dictionary[i] for i in dictionary]

        # words_list = {}
        #
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     if sorted_word not in words_list:
        #         words_list[sorted_word] = [word]
        #     else:
        #         words_list[sorted_word] += ([word])
        # return [words_list[i] for i in words_list]