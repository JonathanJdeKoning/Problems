class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque([])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    q.append((i,j))
        safeness = -1
        seen = set()
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        while q:
            safeness += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in seen: continue
                seen.add(curr)
                i,j = curr
                grid[i][j] = -safeness

                for dy, dx in directions:
                    y = i+dy
                    x = j+dx

                    if min(y,x)<0 or y==R or x==C or (y,x) in seen: continue
                    q.append((y,x))
        h = [(grid[0][0], (0,0))]
        seen = set()
        best = grid[0][0]
        while h:
            currWeight, (y,x) = heapq.heappop(h)
            if (y,x) in seen: continue
            seen.add((y,x))
            best = max(best, currWeight)
            if (y,x) == (R-1,C-1):
                return -best
            for dy, dx in directions:
                newY = y+dy
                newX = x+dx

                if min(newY, newX)<0 or newY==R or newX==C or (newY,newX) in seen: continue
                heapq.heappush(h,(grid[newY][newX], (newY, newX)))


        

