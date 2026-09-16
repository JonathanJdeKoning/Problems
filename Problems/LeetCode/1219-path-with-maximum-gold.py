class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        mx = 0
        R,C = len(grid), len(grid[0])

        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        def dfs(i,j):
            if min(i,j) < 0 or i==R or j == C or grid[i][j] == 0:
                return 0
            init = grid[i][j]
            cellGold = grid[i][j]

            grid[i][j] = 0


            for dy, dx in directions:
                y = i+dy
                x = j + dx
                cellGold = max(init+dfs(y,x), cellGold)
            grid[i][j] = init
            return cellGold

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                mx = max(mx, dfs(i,j))




        return mx
