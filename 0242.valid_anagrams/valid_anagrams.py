from typing import List

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

