class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.coords = {}
        self.grid = grid
        self.n = len(grid)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                self.coords[cell] = (i,j)

    def adjacentSum(self, value: int) -> int:
        y,x = self.coords[value]
        ans = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for dy, dx in directions:
            newY = y + dy
            newX = x+dx
            if min(newY, newX) == -1 or max(newY, newX) == self.n: continue
            ans += self.grid[newY][newX]
        return ans


    def diagonalSum(self, value: int) -> int:
        y,x = self.coords[value]
        ans = 0
        directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dy, dx in directions:
            newY = y + dy
            newX = x+dx
            if min(newY, newX) == -1 or max(newY, newX) == self.n: continue
            ans += self.grid[newY][newX]
        return ans


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)