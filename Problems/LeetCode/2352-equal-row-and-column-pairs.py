class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = R
        cols = []
        for i in range(R):
            cols.append([row[i] for row in grid])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i] == cols[j]:
                    ans += 1
        return ans