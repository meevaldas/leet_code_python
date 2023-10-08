from typing import List

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # list_s = list(s)
        # list_s.sort()
        # list_t = list(t)
        # list_t.sort()
        # return list_s == list_t
        reverse_word = s[::-1]
        return s == reverse_word
