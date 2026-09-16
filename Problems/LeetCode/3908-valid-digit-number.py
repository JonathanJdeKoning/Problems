class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        if s[0] == str(x): return False
        return str(x) in s