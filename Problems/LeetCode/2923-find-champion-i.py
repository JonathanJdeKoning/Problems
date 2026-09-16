class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i,per in enumerate(grid):
            if per.count(1) == len(per)-1: return i