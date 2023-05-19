"""
Given an integer array nums and an integer k, return the number of pairs (i, j)
where i < j such that |nums[i] - nums[j]| == k.
"""

from typing import List

class Solution:
    def count_k_difference(self, nums: List[int], k: int) -> int:

        li = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    li += 1

        return li

