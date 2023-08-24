"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""
from typing import List


class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1

        freq = [value for key, value in freq.items()]
        max_freq = max(freq)
        max_freq_tasks = freq.count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)

