class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = {}
        cols = {}

        for i in range(len(grid)):
            rows[i] = max(grid[i])

        for j in range(len(grid[0])):
            col = [row[j] for row in grid]
            cols[j] = max(col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                best = min(rows[i], cols[j])
                ans += best - grid[i][j]

        return ans