"""
Given an integer array nums and an integer k, return the k most frequent elements. You may
return the answer in any order.
"""
import collections
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary = {}
        # num_counter = 0
        #
        # for num in nums:
        #     if num in dictionary:
        #         num_counter += dictionary[num]
        #         num_counter += num_counter
        #
        #     if dictionary.get(num) is None:
        #         dictionary[num] = 0
        #
        #
        #     return

        counter = collections.Counter(nums).most_common(k)
        return list(lambda x: x[0], counter)
