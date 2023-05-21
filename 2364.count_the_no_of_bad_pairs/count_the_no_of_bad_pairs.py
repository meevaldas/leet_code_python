"""
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j
and j - i != nums[j] - nums[i]. Return the total number of bad pairs in nums.
"""
from typing import List


class Solution:
    def count_bad_pairs(self, nums: List[int]) -> int:
        counter = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (j - i) != (nums[j] - nums[i]):
                    counter += 1
        return counter

