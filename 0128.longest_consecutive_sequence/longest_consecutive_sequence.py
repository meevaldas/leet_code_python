"""
Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence. You must write an algorithm that runs in O(n) time.
"""
from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if it is the start of a  sequence
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
