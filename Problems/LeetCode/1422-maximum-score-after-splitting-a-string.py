class Solution:
    def maxScore(self, s: str) -> int:
        mx = 0
        for i in range(1, len(s)):
            mx = max(mx, s[:i].count("0") + s[i:].count("1"))
        return mx