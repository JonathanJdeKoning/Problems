class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = 0
        rotting = []

        for i in range(R):
            for j in range(C):
                cell = grid[i][j]

                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    rotting.append((i,j))
        
        if not fresh: return 0
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        q= deque(rotting)
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                cy, cx = q.popleft()

                if grid[cy][cx] == 1:
                    grid[cy][cx] = 2
                    fresh -= 1
                    if not fresh: return minutes

                for dy, dx in directions:
                    ny, nx = dy+cy, cx+dx

                    if min(ny,nx) == -1 or ny==R or nx==C: continue
                    if grid[ny][nx] != 1: continue
                    q.append((ny,nx))
        return -1


