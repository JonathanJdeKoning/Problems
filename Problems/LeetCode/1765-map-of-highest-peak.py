class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        steps = -1
        R, C = len(isWater), len(isWater[0])
        water=[]
        newWater = [[None]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if isWater[i][j]:
                    water.append((i,j))
        q = deque(water)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        seen = set()
        while q:
            steps += 1
            for _ in range(len(q)):
                cy, cx = q.popleft()
                if (cy, cx) in seen: continue
                seen.add((cy,cx))
                newWater[cy][cx] = steps
                for dy, dx in directions:
                    ny, nx = cy+dy, dx+cx

                    if min(ny, nx) == -1 or ny==R or nx == C or (ny, nx) in seen: continue

                    q.append((ny,nx))



        return newWater
