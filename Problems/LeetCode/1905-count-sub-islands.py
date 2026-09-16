class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R,C = len(grid1), len(grid1[0])
        ans = 0 
        seen = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                if (i,j) in seen: continue

                if cell == 1:
                    good = True

                    q = deque([(i,j)])

                    while q:
                        currY, currX = q.popleft()
                        if grid1[currY][currX]==0: good = False

                        if (currY, currX) in seen: continue
                        seen.add((currY, currX))

                        for dy, dx in directions:
                            y, x =dy+currY, dx+currX
                            if min(y,x) ==-1 or y==R or x==C or grid2[y][x] == 0 or (y,x) in seen: continue

                            q.append((y,x))
                    if good: ans+= 1
        return ans



