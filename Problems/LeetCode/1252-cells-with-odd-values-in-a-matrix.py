class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = []
        for i in range(m):
            mat.append([0]*n)
        
        for y,x in indices:
            mat[y] = [x+1 for x in mat[y]]
            for i, row in enumerate(mat):
                mat[i][x] += 1



        total = 0
        for row in mat:
            for pos in row:
                if pos%2==1: total += 1
        return total