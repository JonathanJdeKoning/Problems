class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        top = 0
        for row in grid:
            for val in row:
                if val != 0: top += 1

        xaxis = sum([max(x) for x in grid])
        yaxis = 0
        for i in range(cols):
            col = [x[i] for x in grid]
            yaxis += max(col)



        return top+xaxis+yaxis