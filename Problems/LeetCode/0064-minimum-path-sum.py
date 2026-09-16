class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C=  len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if (i,j) == (0,0): continue
                left = float('inf')
                up = float("inf")
                if j != 0:
                    left = grid[i][j-1]
                if i != 0:
                    up = grid[i-1][j]

                grid[i][j] += min(up, left)
        return grid[-1][-1]
