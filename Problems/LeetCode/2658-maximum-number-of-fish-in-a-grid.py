class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def getSumAndExhaust(y,x):
            tot = 0
            tot += grid[y][x]
            grid[y][x] = 0
            
            for dy, dx in directions:
                ny, nx = dy + y, dx + x
                if ny not in range(R) or nx not in range(C): continue
                if grid[ny][nx] == 0: continue 
                
                tot += getSumAndExhaust(ny, nx)
            return tot
            
        
        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                if cell == 0: continue
                
                ans = max(ans, getSumAndExhaust(i,j))
        return ans