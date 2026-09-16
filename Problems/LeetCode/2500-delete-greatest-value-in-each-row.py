class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid[0])):
            mx = 0
            for row in grid:
                temp = max(row)
                row.remove(temp)
                mx = max(temp, mx)
            total += mx
        return total
                

