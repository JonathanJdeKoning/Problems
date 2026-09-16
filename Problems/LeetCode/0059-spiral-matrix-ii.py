class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        R, C = n, n
        matrix = [[0]*n for _ in range(n)]
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
        curr = 1
        while curr <= n**2:
            matrix[y][x] = curr
            curr += 1
            seen.add((y, x))
            ny, nx = dy + y, dx + x
            if ny >= R or nx >= C or ny < 0 or nx < 0 or (ny, nx) in seen:
                dy, dx = mp[(dy, dx)]
                ny, nx = y+dy, x+dx
            y, x = ny, nx
        return matrix