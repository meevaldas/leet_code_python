"""
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most
significant to least significant in left-to-right order. The large integer does
not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits = self.plus_one(digits[:-1])
            digits.append(0)
            return digits
