"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)
        if x > y:
            self.find_median_sorted_arrays(nums2, nums1)

        start, end = 0, x
        while start <= end:
            partition_of_x = (start + end) // 2
            partition_of_y = ((x + y + 1) // 2) - partition_of_x

            # setting partition of x
            max_left_x = float("-inf") if partition_of_x == 0 else nums1[partition_of_x - 1]
            min_right_x = float("inf") if partition_of_x == x else nums1[partition_of_x]

            # setting partition of y
            max_left_y = float("-inf") if partition_of_y == 0 else nums2[partition_of_y - 1]
            min_right_y = float("inf") if partition_of_y == y else nums2[partition_of_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                end = partition_of_x - 1
            else:
                start = partition_of_x +1





