class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx = 0
        idx = 0
        for i, row in enumerate(mat):
            if row.count(1) > mx:
                mx = row.count(1)
                idx = i
        return [idx,mx]

        