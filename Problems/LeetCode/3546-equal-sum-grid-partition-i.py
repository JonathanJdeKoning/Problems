class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        tot = sum([sum(row) for row in grid])
        if tot%2 == 1: return False

        R, C = len(grid), len(grid[0])
        for i in range(R): 
            for j in range(C):
                if i != 0:
                    grid[i][j] += grid[i-1][j]
                if j != 0:
                    grid[i][j] += grid[i][j-1]

                if j!=0 and i != 0:
                    grid[i][j] -= grid[i-1][j-1]



        for j in range(C-1):
            if grid[-1][j] == tot//2:
                return True

        for i in range(R-1):
            if grid[i][-1] == tot//2:
                return True
        for row in grid: print(row)
        return False