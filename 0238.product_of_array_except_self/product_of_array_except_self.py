"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import itertools
import math
import operator
from typing import List


class Solution:

    def product_except_self(self, nums: List[int]) -> List[int]:
        # left = list(itertools.accumulate(nums, operator.mul))
        # left.insert(0, 1)
        #
        # right = list(itertools.accumulate(reversed(nums), operator.mul))
        # right.insert(0, 1)
        #
        # return [left[index] * right[-index - 2] for index in range(len(nums))]

        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right_product = 1

        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        return res
