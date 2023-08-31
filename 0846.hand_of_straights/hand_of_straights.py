"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if
she can rearrange the cards, or false otherwise.
"""
from typing import List
import heapq


class Solution:
    def is_n_straight_hand(self, hand: List[int], group_size: int) -> bool:
        if len(hand) % group_size:
            return False

        count={}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(first, first + group_size):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
