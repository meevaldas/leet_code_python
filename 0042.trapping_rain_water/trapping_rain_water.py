"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # check whether the list is empty
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result
