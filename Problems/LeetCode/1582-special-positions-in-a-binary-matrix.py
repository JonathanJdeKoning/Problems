class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        total = 0
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                pos = mat[i][j]
                if pos == 1:
                    if mat[i].count(0) == cols-1:
                        if [x[j] for x in mat].count(0) == rows-1:
                            total += 1
        return total