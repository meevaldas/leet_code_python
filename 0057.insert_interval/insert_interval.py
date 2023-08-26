"""
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                new_interval = [min(new_interval[0],intervals[i][0]), max(new_interval[1],intervals[i][1])]
        res.append(new_interval)
        return res
