class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = len(mat)
        total = 0
        for i in range(x):
            total += mat[i][i]
            total += mat[i][-(i+1)]
        if x%2==1:
            total -= mat[x//2][x//2] 
        return total