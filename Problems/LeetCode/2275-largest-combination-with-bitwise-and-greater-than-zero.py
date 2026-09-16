class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max({i: sum([int(row[i]) for row in[bin(c)[2:].zfill(30) for c in candidates]]) for i in range(30)}.values())