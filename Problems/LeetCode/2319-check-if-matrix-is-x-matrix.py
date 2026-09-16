class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        diags = []

        for i in range(len(grid)):
            diags.append([i,i])
            diags.append([i, (len(grid)-1)-i])
        for i in range(len(grid)):
            for j in range(len(grid)):
                pos = grid[i][j]
                if [i,j] in diags:
                    if pos == 0: return False
                else:
                    if pos != 0: return False
        return True
