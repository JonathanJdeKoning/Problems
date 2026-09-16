class Solution:
    def minMoves(self, matrix: List[str]) -> int:  
        R, C = len(matrix), len(matrix[0])
        if matrix[R-1][C-1] == "#": return -1
        directions = list(pairwise([-1,0,1,0,-1]))
        
        tps = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell not in ".#":
                    tps[cell].append((i,j))


        q = deque([(0, R-1, C-1)])
        if matrix[R-1][C-1] not in ".#":
            for ty, tx in tps[matrix[R-1][C-1]]:
                q.append((0,ty,tx))
                
        seen = set()
        while q:
            cc, cy, cx = q.popleft()
            if (cy, cx) in seen: continue
            seen.add((cy,cx))

            if (cy, cx) == (0,0): return cc

            if matrix[cy][cx] != ".":
                for ty, tx in tps[matrix[cy][cx]]:
                    if (ty,tx) not in seen:
                        q.appendleft((cc, ty, tx))
                del tps[matrix[cy][cx]]

            for dy, dx in directions:
                ny, nx = cy+dy, cx+dx

                if min(ny, nx) == -1 or ny == R or nx == C: continue
                if (ny, nx) in seen: continue
                if matrix[ny][nx] == "#": continue
                
                q.append((cc+1, ny, nx))
                continue
                
               
        return -1