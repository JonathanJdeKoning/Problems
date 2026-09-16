class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                midParent = matrix[i-1][j]

                leftParent = inf
                rightParent = inf

                if j != 0:
                    leftParent = matrix[i-1][j-1]

                if j != N-1:
                    rightParent = matrix[i-1][j+1]

                optimalValue = matrix[i][j] + min(leftParent, midParent, rightParent)

                matrix[i][j] = optimalValue
        return min(matrix[-1])

            






            




