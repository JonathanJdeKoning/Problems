class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        diagsU = {}
        diagsD = {}
        for i in range(n):
            for j in range(n):
                diagsU[(i,j)] = i+j
                diagsD[(i,j)] = (i-j) + (i-j)


        @cache
        def onDiag(y1, x1, y2, x2):
            res = diagsU[(y1,x1)] == diagsU[(y2, x2)] or diagsD[(y1,x1)] == diagsD[(y2, x2)]
            return res


        ans = []
        current = []
        def addSolution():
            nonlocal current
            grid = [["."]*n for _ in range(n)]
            for i in range(len(current)):
                grid[i][current[i]] = "Q"
            ans.append(copy.deepcopy(["".join(row) for row in grid]))

        def findSolution(i):
            nonlocal current
            if i == n:
                addSolution()
                return
            for j in range(n):
                if j in current: continue
                if any([onDiag(i,j, y2,x2) for y2,x2 in enumerate(current)]): continue
                current.append(j)
                findSolution(i+1)
                current.pop()

        
        findSolution(0)
        return ans


