class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        #m=R, n=C
        ans = [[None]*(C-k+1) for _ in range(R-k+1)]
        for i in range(R - k + 1):
            for j in range(C - k + 1):
                print(i,j)
                mat = set()
                for kk in range(i, i+k):
                    for ll in range(j, j+k):
                        print(kk,ll)
                        mat.add(grid[kk][ll])
                
                if len(mat) == 1: ans[i][j] = 0
                else:
                    ans[i][j] = min((b - a for a,b in pairwise(sorted(mat))))
        return ans
                
                
        