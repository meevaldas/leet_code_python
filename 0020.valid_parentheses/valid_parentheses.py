"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        # hashmap
        close_parentheses = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close_parentheses: # it will be a closing one
                if stack and stack[-1] == close_parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
