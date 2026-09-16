class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        x, y = y,x
        for i in range(y, y+(k//2)):
            for j in range(x, x+k):
                grid[i][j], grid[(y+k-1)-(i-y)][j] = grid[(y+k-1)-(i-y)][j], grid[i][j]
        return grid