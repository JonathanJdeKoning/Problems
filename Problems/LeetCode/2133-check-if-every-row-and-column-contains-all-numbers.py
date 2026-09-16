class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            if sorted(matrix[i]) != list(range(1,n+1)): return False
            if sorted([x[i] for x in matrix]) != list(range(1, n+1)): return False
        return True