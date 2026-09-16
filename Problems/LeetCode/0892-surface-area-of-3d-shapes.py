class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        total = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val != 0:
                    total += 2
                for dy,dx in directions:
                    y = i+dy
                    x = j+dx
                    if min(y,x)==-1 or max(y,x)==n:
                        total += val
                    else:
                        total += max(val-grid[y][x],0)
        return total
                        


