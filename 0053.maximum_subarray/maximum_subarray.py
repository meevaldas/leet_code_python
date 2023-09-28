"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.
"""
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
