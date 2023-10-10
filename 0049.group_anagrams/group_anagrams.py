"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
import collections
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary = {}
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     # If word is not in dictionary
        #     if sorted_word not in dictionary:
        #         dictionary[sorted_word] = [word]
        #     # If previously it is present that means its anagram
        #     # was previously present
        #     else:
        #         dictionary[sorted_word] += [word]
        # return [dictionary[i] for i in dictionary]
        # dic = collections.defaultdict(list)
        # for word in strs:
        #     dic[''.join(sorted(word))].append(word)
        # return dic.values()
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return sorted(list(ans.values()))

