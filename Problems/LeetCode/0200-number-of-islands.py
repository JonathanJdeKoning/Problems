class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        ans = 0

        def exhaust(y, x):
            grid[y][x] = "0"
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx

                if ny not in range(R) or nx not in range(C):
                    continue
                if grid[ny][nx] == "0":
                    continue
                exhaust(ny, nx)

        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                if cell == "1":
                    ans += 1
                    exhaust(i, j)

        return ans