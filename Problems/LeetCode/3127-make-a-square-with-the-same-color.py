class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i, row in enumerate(grid[:-1]):
            for j, cell in enumerate(row[:-1]):
                vals = Counter([grid[i][j],grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]).values()
                if 3 in vals or 4 in vals: return True
        return False
