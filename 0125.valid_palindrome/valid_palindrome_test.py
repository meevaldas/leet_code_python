import unittest
from valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome_example_one(self):
        self.assertAlmostEqual(Solution().is_palindrome("A man, a plan, a canal: Panama"), True)

    def test_valid_palindrome_example_two(self):
        self.assertAlmostEqual(Solution().is_palindrome("race a car"), False)

    def test_valid_palindrome_example_three(self):
        self.assertAlmostEqual(Solution().is_palindrome(" "), True)
