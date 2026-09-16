class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        mx = 0
        for i in range(R-2):
            for j in range(C-2):
                v = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                mx = max(mx, v)
        return mx