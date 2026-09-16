class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negs = 0
        tot = 0
        mn = abs(matrix[0][0])
        for row in matrix:
            absrow = [abs(x) for x in row]
            negs += len([x for x in row if x < 0])
            mn = min(mn, min(absrow))
            tot += sum(absrow)
     
        return tot - (2*mn)*(negs%2)
