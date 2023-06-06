"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such
that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
from typing import List


class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        # to get the index and value we use enumerate
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temperature, stack_index = stack.pop()
                answer[stack_index] = (index - stack_index)
            stack.append([temperature, index])
        return answer
