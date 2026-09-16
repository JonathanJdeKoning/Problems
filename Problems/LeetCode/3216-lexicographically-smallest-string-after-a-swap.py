class Solution:
    def getSmallestString(self, s: str) -> str:
        for i, (a, b) in enumerate(pairwise(s)):
            a = int(a)
            b = int(b)
            if b%2 == a%2 and a > b:
                return s[:i] + str(b)+str(a) + s[i+2:]
        return s
