class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        cols = {}
        for i, cell in enumerate(grid[0]):
            cols[i] = [0,0]
        
        ans = 0
        for i, row in enumerate(grid):
            Xs = 0
            Ys = 0
            for j, cell in enumerate(row):
                prevX, prevY = cols[j]
                Xs += prevX
                Ys += prevY
                if cell == "X":
                    Xs += 1
                    cols[j][0] += 1
                if cell == "Y":
                    Ys += 1
                    cols[j][1]+=1

                if Xs == 0: continue
                if Xs != Ys: continue
                ans += 1
        return ans