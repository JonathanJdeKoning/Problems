class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = 0
        cols = 0
        for row in grid:
            for a,b in zip(row, row[::-1]):
                if a!=b:
                    rows += 1

        new = []
        for i in range(len(grid[0])):
            new.append([x[i] for x in grid])


        for col in new:
            for a,b in zip(col, col[::-1]):
                if a!=b:
                    cols += 1

        return min(rows//2, cols//2)