"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.You may assume that each input would
have exactly one solution, and you may not use the same element twice.You can return
the answer in any order.
"""

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            comp = target - num

            if comp in hash_map:
                return [hash_map[comp], index]

            hash_map[num] = index
