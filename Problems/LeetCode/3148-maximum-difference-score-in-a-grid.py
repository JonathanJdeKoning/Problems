class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        dp = []
        for _ in range(R):
            dp.append([-1]*C)
        dp[0][0] = 0
        mx = -inf
        must = -inf
        used = False
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                up,left,upMX,leftMX = 0,0,0,0
                poss = [0]
                cellMX = 0
                if i != 0:
                    up,upMX = grid[i-1][j],dp[i-1][j]
                    upGood = (cell-up)+upMX
                    if upGood > cellMX:
                        cellMX = upGood
                        used = True
                    must = max(upGood, must)
                if j!=0:
                    left,leftMX = grid[i][j-1],dp[i][j-1]
                    leftGood = (cell-left)+leftMX
                    if leftGood > cellMX:
                        cellMX = leftGood
                        used = True
                    must = max(leftGood, must)

                mx = max(mx, cellMX)
                dp[i][j] = cellMX
        if used:
            return mx
        else:
            return must
                
                