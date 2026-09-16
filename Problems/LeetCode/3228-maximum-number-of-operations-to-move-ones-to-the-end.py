class Solution:
    def maxOperations(self, s: str) -> int:
        total, c = 0, 0
        for k, v in groupby(s, int):
            c += len(list(v)) * k
            total += c * (1-k)
        return total