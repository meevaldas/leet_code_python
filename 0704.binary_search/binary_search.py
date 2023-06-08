"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = left + ((right - left) // 2)
            if nums[mid_index] < target:
                left = mid_index + 1
            elif nums[mid_index] > target:
                right = mid_index - 1
            else:
                return mid_index
        return -1
