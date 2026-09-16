class Solution:
    def isPalindromic(self, s: str) -> bool:
        b = "".join([bin(ord(c))[2:].zfill(8) for c in s])
        print(b)
        return b == b[::-1]