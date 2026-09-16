class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if k >= n and k >= m: return 0
        cut = max(n,m)
        if cut > k:
            return k*(cut-k)