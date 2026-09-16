class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        out = []
        for i in range(len(grid[0])):
            out.append(len(max([str(x[i]) for x in grid],key=lambda x:len(x))))
        return out
