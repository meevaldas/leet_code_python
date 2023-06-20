"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        # check three conditions
        #   if open == close == n
        #   if open < n (we can add the open parantheses)
        #   if closed < opened (add closed parantheses)
        stack = []
        result = []

        def back_track(open_n, close_n):
            if open_n == close_n == n:
                result.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                back_track(open_n + 1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(")")
                back_track(open_n, close_n + 1)
                stack.pop()

        back_track(0, 0)
        return result
