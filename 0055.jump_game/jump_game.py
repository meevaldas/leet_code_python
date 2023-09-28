"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        right = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > right:
                return False
            if nums[i] + i > right:
                right = nums[i] + i
            if right >= last:
                return True
