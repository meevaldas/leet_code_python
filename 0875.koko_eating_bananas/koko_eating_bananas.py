"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile
has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import math
from typing import List


class Solution:
    def min_eating_speed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles)

        while left <= right:
            total_time = 0
            k = (left + right) // 2
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1
        return result
