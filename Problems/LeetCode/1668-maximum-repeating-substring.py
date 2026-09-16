class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(100,-1,-1):
            if word*i in sequence: return i
        return 0