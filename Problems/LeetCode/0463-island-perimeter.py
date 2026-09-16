class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mat = []
        mat.append([0]*(cols+2))
        for row in grid:
            mat.append([0]+row+[0])
        mat.append([0]*(cols+2))
        total = 0
        for i, row in enumerate(mat):
            for j, pos in enumerate(row):
                if mat[i][j] == 0: continue
                good = 4
                up = mat[i-1][j]
                down = mat[i+1][j]
                left = mat[i][j-1]
                right = mat[i][j+1]
                dx = [up,down,left,right]
                total += good - dx.count(1)
        return total