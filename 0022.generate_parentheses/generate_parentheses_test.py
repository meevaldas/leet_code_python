import unittest
from generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().generate_parenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().generate_parenthesis(1), ["()"])
