class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                right = None
                down = None
                try:
                    right = grid[i][j+1]
                except:
                    pass
                
                try:
                    down = grid[i+1][j]
                except:
                    down = cell
                
                
                if cell == down and cell != right:
                    continue
                else:
                    return False
        return True