import unittest
from evaluate_reverse_polish_notation import Solution


class TestEvaluateReverseNotation(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().eval_rpn(["2", "1", "+", "3", "*"]), 9)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().eval_rpn(["4", "13", "5", "/", "+"]), 6)

    def test_example_three(self):
        self.assertAlmostEqual(
            Solution().eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
