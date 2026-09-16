class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        dsu = DisjointSetUnion((R*C)+1)

        for row in grid:
            if 1 in row: break
        else: return 1

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    uuid = i*C+j
                    dsu.size[uuid] = 1

        seen = set()
        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                if not cell: continue
                if (i,j) in seen: continue
                base = i*C+j
                dfs = deque([(i,j)])

                while dfs:
                    cy, cx = dfs.pop()
                    uuid = cy*C+cx
                    if base != uuid:
                        dsu.union(uuid, base)
                    if (cy,cx) in seen: continue
                    seen.add((cy,cx))

                    for dy, dx in directions:
                        ny, nx = cy+dy, cx+dx
                        if min(ny, nx) == -1 or ny==R or nx==C: continue
                        if not grid[ny][nx]: continue
                        if (ny,nx) in seen: continue
                        dfs.append((ny, nx))
        ans = 1
        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                if cell:
                    continue
                groups = set()
                for dy, dx in directions:
                    ny, nx = dy+i, dx+j

                    if min(ny, nx) == -1 or ny == R or nx == C: continue
                    if not grid[ny][nx]: continue
                    uuid = ny*C+nx
                    groups.add(dsu.find(uuid))
                sizes = [dsu.set_size(g) for g in groups]
                ans = max(ans, 1+sum(sizes))
        return max(ans, max(dsu.size))








