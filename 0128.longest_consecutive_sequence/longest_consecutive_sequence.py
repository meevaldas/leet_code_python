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
            if (n - 1) not in num_set:
                index = 0
                while (n + index) in num_set:
                    index += 1
                longest = max(index, longest)
        return longest
