class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        out = []
        seen = set()
        for i, row in enumerate(land):
            for j, cell in enumerate(row):
                if cell == 1 and (i,j) not in seen:
                    q = deque([(i,j)])
                    xs = []
                    ys = []
                    while q:
                        curr = q.popleft()
                        if curr in seen: continue
                        seen.add(curr)
                        currX = curr[1]
                        currY = curr[0]
                        xs.append(currX)
                        ys.append(currY)

                        for dy, dx in directions:
                            y = currY + dy
                            x = currX + dx

                            if y <0 or x<0 or y==rows or x==cols or (y,x) in seen or land[y][x]==0: continue
                            q.append((y,x))
                    out.append([min(ys), min(xs), max(ys), max(xs)])
        return out
