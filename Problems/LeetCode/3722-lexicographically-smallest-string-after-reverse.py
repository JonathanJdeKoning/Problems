class Solution:
    def lexSmallest(self, s: str) -> str:
        best = s
        for i in range(len(s)):
            first = s[:i][::-1] + s[i:]
            last = s[:i] + s[i:][::-1]
            best = min(best, first)
            best = min(best, last)
        return best
        