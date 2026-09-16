class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])
        vals = []
        
        for i in range(R):
            for j in range(C):
                vals.append(grid[i][j])
        if len(set([z%x for z in vals])) != 1: return -1
        vals.sort()
        mid = len(vals) // 2
        m = vals[mid]
        

        for v in vals:
            ans += abs(v - m) // x
        return ans







                