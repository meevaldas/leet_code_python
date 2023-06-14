"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


# class Solution:
#     def max_profit(self, prices: List[int]) -> int:
#         left = 0
#         right = left + 1
#         result = 0
#
#         while left < right:
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 result = max(result, profit)
#             else:
#                 left += 1
#             right += 1
#         return result


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        low_stock = float("inf") # setting value to +infinity

        for price in prices:
            if low_stock > price:
                low_stock = price
            elif price - low_stock > profit:
                profit = price - low_stock
        return profit
