"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import math
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        prod_list = []

        for i in range(len(nums)):
            left_prod = math.prod(nums[0:i])
            right_prod = math.prod(nums[i+1:])
            total = left_prod * right_prod
            prod_list.append(total)
        return prod_list


