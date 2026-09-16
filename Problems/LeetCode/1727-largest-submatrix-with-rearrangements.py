class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        def largest(heights):
            ans = 0
            for i, h in enumerate(heights):
                ans = max(ans, h*(i+1))
            return ans
        R, C = len(matrix), len(matrix[0])
        for i in range(1,R):
            for j in range(C):
                if matrix[i][j] == 0: continue
                matrix[i][j] += matrix[i-1][j]
        ans = 0
        for row in matrix:
            ans = max(ans, largest(sorted(row, reverse=True)))
        return ans