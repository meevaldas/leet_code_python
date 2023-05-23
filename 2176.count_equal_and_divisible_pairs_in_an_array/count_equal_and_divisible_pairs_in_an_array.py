"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
"""
import collections
import itertools
from typing import List


class Solution:
    # Author: Ananthu Sudhikumar
    def count_pairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        cache = collections.defaultdict(list)

        for index, num in enumerate(nums):
            cache[num].append(index)

        for indices in cache.values():
            if len(indices) < 2:
                continue

            for i, j in itertools.combinations(indices, 2):
                if (i * j) % k == 0:
                    pairs += 1
        return pairs

    # Author: Meeval Das
    # def count_pairs(self, nums: List[int], k: int) -> int:
    #     pair_counter = 0
    #
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j] and (i * j) % k == 0:
    #                 pair_counter += 1
    #     return pair_counter

