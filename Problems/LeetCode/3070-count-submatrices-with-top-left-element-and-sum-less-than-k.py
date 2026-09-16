class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
    
        ans = 0
        for i in range(R):
            for j in range(C):
                if i != 0:
                    grid[i][j] += grid[i-1][j]
                if j != 0:
                    grid[i][j] += grid[i][j-1]
                if i!= 0 and j != 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    ans += 1

        return ans



