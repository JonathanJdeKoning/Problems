class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        ans = sum(matrix[0][1:]) + sum(row[0] for row in matrix)

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0: continue
                val = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                matrix[i][j] = val
                ans += val
        return ans