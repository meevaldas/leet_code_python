"""
Given an array of meeting time intervals where intervals[i] = [starti,endi], determine if a person could attend all meetings.
"""
from typing import List


class Solution:
    def can_attend_meetings(self, intervals):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
