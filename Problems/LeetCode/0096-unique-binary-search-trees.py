class Solution:

    def numTrees(self, n: int) -> int:
        @cache
        def treeCount(n, mn, mx):
            if mn > mx: return 1
            ans = 0
            for t in range(mn, mx+1):
                ans += treeCount(t, mn, t-1) * treeCount(t, t+1, mx)
            return ans

        return treeCount(n-1, 0, n-1)

