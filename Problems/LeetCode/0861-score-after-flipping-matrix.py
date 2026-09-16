class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if row[0] == 0:
                new = []
                for c in row:
                    if c == 0:
                        new.append(1)
                    else:
                        new.append(0)
                grid[i] = new

        for i in range(1,len(grid[0])):
            col = [x[i] for x in grid]
            if col.count(0) > col.count(1):
                for currRow, row in enumerate(grid):
                    if row[i] == 0:
                        grid[currRow][i] = 1
                    else:
                        grid[currRow][i] = 0
        return sum([int("".join([str(x) for x in row]),2) for row in grid])