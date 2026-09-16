class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        R, C = len(img1), len(img1[0])
        def posShift(grid, y, x):
            nonlocal R, C
            return [[0]*C for _ in range(y)] + [[0]*x + row[:C-x] for row in grid][:R-y]
        def negShift(grid, y, x):
            nonlocal R, C
            return  [row[x:] + [0]*x for row in grid][y:]+ [[0]*C for _ in range(y)]

        def shift(grid, y, x):
            if y < 0:
                new = negShift(grid, -y, 0)
            elif y > 0:
                new = posShift(grid, y, 0)
            else: 
                new = grid

            if x < 0:
                new = negShift(new, 0, -x)
            elif x > 0:
                new = posShift(new, 0, x)
            return new
            
        ans = 0
        for ys in range(-R, R):
            for xs in range(-C, C):
                new = shift(img1, ys, xs)
                
                overlap = 0
                for i in range(R):
                    for j in range(C):
                        if new[i][j] and img2[i][j]:
                            overlap += 1

                ans = max(ans, overlap)

                
        return ans
