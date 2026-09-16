class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        palindrome = list(palindrome)
        m = len(palindrome) // 2
        for i, c in enumerate(palindrome):
            if c == "a": continue
            if c != "a" and i == m and len(palindrome) %2 ==1:
                continue
            palindrome[i] = "a"
            return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)
