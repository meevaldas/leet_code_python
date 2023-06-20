import unittest
from valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test_valid_example_one(self):
        self.assertAlmostEqual(Solution().is_valid("()"), True)

    def test_valid_example_two(self):
        self.assertAlmostEqual(Solution().is_valid("()[]{}"), True)

    def test_valid_example_three(self):
        self.assertAlmostEqual(Solution().is_valid("(]"), False)
