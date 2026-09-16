class Solution:
    def minimumMoves(self, s: str) -> int:
        total = 0
        start = 0
        while start < len(s):
            if s[start] == "X":
                total += 1
                start += 3
            else:
                start += 1
        return total