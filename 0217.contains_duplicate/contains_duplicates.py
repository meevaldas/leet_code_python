from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
