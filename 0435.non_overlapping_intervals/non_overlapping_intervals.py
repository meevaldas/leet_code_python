"""
Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
from typing import List


class Solution:
    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        remove = 0
        previous_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                remove += 1
                previous_end = min(end, previous_end)
        return remove




