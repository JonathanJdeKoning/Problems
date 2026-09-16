class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l = inf
        r = -inf
        u = inf
        d = -inf

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    l = min(l,j)
                    r = max(r,j)
                    u = min(u,i)
                    d = max(d,i)
                    
        return (abs(u-d)+1)*(abs(l-r)+1)                    
                