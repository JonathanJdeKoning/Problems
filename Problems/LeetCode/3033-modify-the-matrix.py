class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        newmat = []
        for i, row in enumerate(matrix):
            newrow = [0]*cols
            for j, x in enumerate(row):
                if x != -1:
                    newrow[j] = x
                else:
                    newrow[j] = max(x[j] for x in matrix)
            newmat.append(newrow)
        return newmat