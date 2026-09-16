class Solution:
    def scoreBalance(self, s: str) -> bool:
        def charScore(c):
            return ord(c) - 96

        for i in range(len(s)):
            if sum(charScore(c) for c in s[:i]) == sum(charScore(c) for c in s[i:]):
                return True
        return False