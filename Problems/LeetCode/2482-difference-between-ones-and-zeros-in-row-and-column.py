class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = {}
        onesCol = {}
        zerosRow = {}
        zerosCol = {}

        R, C = len(grid), len(grid[0])

        for i in range(R):
            onesRow[i] = grid[i].count(1)
            zerosRow[i] = grid[i].count(0)

        for j in range(C):
            col = [row[j] for row in grid]
            onesCol[j] = col.count(1)
            zerosCol[j] = col.count(0)

        new = []
        for i in range(R):
            row = []
            for j in range(C):
                row.append(onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j])
            new.append(row)
        return new