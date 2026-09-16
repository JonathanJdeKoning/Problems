class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        seen = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1 and (i,j) not in seen:
                    q = deque([(i,j)])
                    island = 0
                    while q:
                        curr = q.popleft()
                        if curr in seen: continue
                        seen.add(curr)
                        island += 1

                        for dy,dx in directions:
                            y = curr[0]+dy
                            x = curr[1]+dx

                            if y<0 or x<0 or y==rows or x==cols or (y,x) in seen or grid[y][x]==0: continue
                            q.append((y,x))
                    mx = max(island,mx)
        return mx