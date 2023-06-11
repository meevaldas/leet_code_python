"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7]
might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
"""
from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = float("inf")

        while left < right:
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return min(result, nums[left])
        # curr_min = float("inf")
        #
        # while start < end:
        #     mid = (start + end) // 2
        #     curr_min = min(curr_min, nums[mid])
        #
        #     # right has the min
        #     if nums[mid] > nums[end]:
        #         start = mid + 1
        #
        #     # left has the  min
        #     else:
        #         end = mid - 1
        #
        # return min(curr_min, nums[start])
