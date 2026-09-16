class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        R, C = len(forest), len(forest[0])
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        trees = {}
        
        for i in range(R):
            for j in range(C):
                cell = forest[i][j]
                if cell > 1:
                    trees[cell] = (i, j)
        order = sorted(list(trees.items()))
        goals = sorted(list(pairwise([(0,0)] + [x[1] for x in order])), key=lambda z:dist(z[0], z[1]), reverse=True)
        totalSteps = 0
        for (sy, sx), (gy, gx) in goals:
    
            q = deque([(sy, sx)])
            seen = set()
            steps = -1
            found = False
            while q and not found:
                steps += 1
                for _ in range(len(q)):
                    cy, cx = q.popleft()
                    if (cy, cx) in seen: continue
                    if (cy, cx) == (gy, gx): 
                        totalSteps += steps
                        found = True

                        break
                    seen.add((cy, cx))
                    for dy, dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if ny >= R or ny <= -1 or nx >= C or nx <= -1: continue
                        if forest[ny][nx] == 0: continue
                        if (ny, nx) in seen: continue
                        q.append((ny, nx))
            
                if found: break
            else:
                return -1



        return totalSteps

