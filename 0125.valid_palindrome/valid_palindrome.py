class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        altered_string = ''.join(filter(str.isalnum, s))
        rev_string = altered_string[::-1]
        if altered_string == rev_string:
            return True
        return False
