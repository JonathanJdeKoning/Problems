class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if grid[0][0] == 1: health -=1
        q = deque([(0,0, health)])
        R, C = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        end = (R-1, C-1)
        seen = set()

        while q:
            curr = q.popleft()
            #print(curr)
            #print(seen)
            currY, currX, currH = curr
            if (currY, currX) in seen: continue
            if currH == 0: continue
            if (currY, currX) == end:
                return True
            seen.add((currY, currX))

            for dy, dx in directions:
                y = currY+dy
                x = currX+dx

                if min(y,x) == -1 or y==R or x==C or (y,x) in seen: continue
                

                val =grid[y][x]
                if val == 1:
                    q.append((y,x,currH-1))
                else:
                    q.appendleft((y,x,currH))
        return False

