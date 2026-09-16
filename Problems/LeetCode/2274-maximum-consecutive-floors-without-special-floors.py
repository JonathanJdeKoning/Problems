class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        diffs = [(b-a)-1 for a,b in pairwise(special)]
        mx = max(diffs, default = 0)
        if special[0] != bottom:
            mx = max(mx, special[0] - bottom)
        if special[-1] != top:
            mx = max(mx, top - special[-1])
        return mx