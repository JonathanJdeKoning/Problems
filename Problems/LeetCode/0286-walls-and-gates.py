class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        R, C = len(rooms), len(rooms[0])
        q = deque()
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        dist = -1
        seen = set()
        while q:
            dist += 1
            for _ in range(len(q)):
                cy, cx = q.popleft()
                if (cy, cx) in seen: continue
                seen.add((cy, cx))
                rooms[cy][cx] = dist

                for dy, dx in directions:
                    ny, nx = dy+cy, dx+cx
                    if ny not in range(R) or nx not in range(C): continue
                    if (ny, nx) in seen: continue
                    if rooms[ny][nx] == -1: continue

                    q.append((ny, nx))
        