class Solution:
    def maxPower(self, s: str) -> int:
        return max([len(x) for x in[list(g) for k, g in groupby(s)]])