class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i, c in enumerate(s):
            total += abs(i-t.index(c))
        return total