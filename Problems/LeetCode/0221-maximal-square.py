class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        ans = min(1, matrix[0].count("1") + [row[0] for row in matrix].count("1"))
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == "0": continue
                val = 1 + min(int(matrix[i][j-1]), int(matrix[i-1][j]), int(matrix[i-1][j-1]))
                ans = max(ans, val)
                matrix[i][j] = val
        return ans**2
