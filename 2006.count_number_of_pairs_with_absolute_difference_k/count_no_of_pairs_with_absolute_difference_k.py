"""
Given an integer array nums and an integer k, return the number of pairs (i, j)
where i < j such that |nums[i] - nums[j]| == k.
"""

from typing import List


class Solution:
    def count_k_difference(self, nums: List[int], k: int) -> int:
        number_counter = {}
        pair_counter = 0

        for num in nums:
            diff_one = num + k
            diff_two = num - k

            if number_counter.get(diff_one):
                pair_counter += number_counter[diff_one]

            if number_counter.get(diff_two):
                pair_counter += number_counter[diff_two]

            if number_counter.get(num) is None:
                number_counter[num] = 0

            number_counter[num] += 1
        return pair_counter

