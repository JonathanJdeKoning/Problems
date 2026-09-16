class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for poss in mat[0]:
            for row in mat[1:]:
                idx = bisect_left(row, poss)
                if idx == len(row) or row[idx] != poss:
                    break
            else:
                return poss
        return -1