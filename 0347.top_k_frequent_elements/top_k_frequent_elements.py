"""
Given an integer array nums and an integer k, return the k most frequent elements. You may
return the answer in any order.
"""
import collections
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).most_common(k)
        return [x[0] for x in counter]
