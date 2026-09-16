class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        ans = []

        y, x = 0,0
        dy, dx = 0,1

        seen = set()
        mp = {
            (0,1) : (1,0),
            (1,0) : (0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1),
        }

        while len(ans) != R*C:
            ans.append(matrix[y][x])
            seen.add((y, x))
            ny, nx = dy + y, dx + x
            if ny >= R or nx >= C or ny < 0 or nx < 0 or (ny, nx) in seen:
                dy, dx = mp[(dy, dx)]
                ny, nx = y+dy, x+dx
            y, x = ny, nx
        return ans
