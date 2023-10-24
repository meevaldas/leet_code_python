"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)
        return result


