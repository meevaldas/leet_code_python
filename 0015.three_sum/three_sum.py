"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
