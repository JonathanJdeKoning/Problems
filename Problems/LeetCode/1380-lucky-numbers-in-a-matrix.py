class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        lucky = []

        for i, row in enumerate(matrix):
            mn = min(row)
            mindex = row.index(mn)

            if mn == max([row[mindex] for row in matrix]):
                lucky.append(mn)


        return lucky

