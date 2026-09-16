class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.lower() if c.isalnum()])
        return s == s[::-1]