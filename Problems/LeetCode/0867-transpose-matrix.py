class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = []
        for i in range(len(matrix[0])):
            new.append([x[i] for x in matrix])
        return new