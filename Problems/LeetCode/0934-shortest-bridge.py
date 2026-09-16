class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        seen = set()
        interior = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inBounds(i, j):
            return i >= 0 and j >= 0 and i < R and j < C

        def exhaustIsland(i, j):
            nonlocal seen
            nonlocal directions
            nonlocal grid
            q = deque([(i, j)])
            seen.add((i, j))
            while q:
                cy, cx = q.popleft()

                for dy, dx in directions:
                    ny, nx = dy+cy, dx+cx
                    if not inBounds(ny, nx): continue
                    if grid[ny][nx] == 0: continue
                    if (ny, nx) in seen: continue
                    seen.add((ny, nx))
                    q.append((ny, nx))

            
        def findFirstIsland():
            for i in range(R):
                for j in range(C):
                    cell = grid[i][j]
                    if cell == 0: continue
                    return (i, j)

        def handleInterior():
            nonlocal grid
            nonlocal seen
            nonlocal interior
            nonlocal directions
            for y, x in seen:
                for dy, dx in directions:
                    ny, nx = y+dy, x+dx
                    if not inBounds(ny, nx): break
                    if grid[ny][nx] == 0: break
                else:
                    interior.add((y,x))
            seen -= interior

        islandY, islandX = findFirstIsland()
        exhaustIsland(islandY, islandX)
        handleInterior()

        q = deque(list(seen))
        print(q)
        steps = -2
        while q:

            steps += 1
            for _ in range(len(q)):
                cy, cx = q.popleft()
                if grid[cy][cx] == 1 and (cy, cx) not in seen: return steps

                seen.add((cy, cx))

                for dy, dx in directions:
                    ny, nx = dy+cy, dx+cx
                    if not inBounds(ny, nx): continue
                    if (ny, nx) in seen: continue
                    if (ny, nx) in interior: continue
                    if grid[ny][nx] == 0:
                        seen.add((ny, nx))
                    q.append((ny, nx))

                    