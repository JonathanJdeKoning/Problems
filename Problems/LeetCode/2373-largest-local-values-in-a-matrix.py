class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        out = []
        for i in range(len(grid)-2):
            row = []
            for j in range(len(grid)-2):
                new = []
                for k in range(3):
                    new.append(grid[i+k][j:j+3])
                row.append(max(max(x) for x in new))
            out.append(row)
        return out