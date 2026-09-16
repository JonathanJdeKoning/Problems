class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = int(1e9)+7
        R, C = len(grid), len(grid[0])
        @cache
        def maxProd(i, j, n=False):
            if i < 0 or j < 0: return None
            if i >= R or j >= C: return None
            x = grid[i][j]

            pos = [x for x in [maxProd(i-1, j, False),maxProd(i, j-1, False)] if x != None]
            neg = [x for x in [maxProd(i-1, j, True), maxProd(i, j-1, True)] if x != None]

            mult=1
            if x >= 0 and not n:
                mult = max(pos, default=1)
            if x >= 0 and n:
                mult = min(neg, default=1)
            if x < 0 and not n:
                mult = min(neg, default=1)
            if x < 0 and n:
                mult = max(pos, default=1)
            

            return x * mult


        ans = maxProd(R-1,C-1, False)
        if ans < 0 :
            return -1

        return ans % MOD
        



            