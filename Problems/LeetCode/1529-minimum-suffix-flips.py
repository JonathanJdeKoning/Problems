class Solution:
    def minFlips(self, target: str) -> int:
        return sum(1 for a, b in pairwise("0" + target) if a != b)