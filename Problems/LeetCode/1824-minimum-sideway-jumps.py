class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        h = [(0, (0,2))]
        seen = set()
        while h:
            jumps, (k, road) = heappop(h)
            if (k,road) in seen: continue
            seen.add((k,road))
            if k == len(obstacles)-1: return jumps
            obst = obstacles[k]
            fut = obstacles[k+1]

            if obst != 1 :
                heappush(h, (jumps+1, (k, 1)))
            if obst != 2:
                heappush(h, (jumps+1, (k, 2)))
            if obst != 3:
                heappush(h, (jumps+1, (k, 3)))
            if fut != road:
                heappush(h, (jumps, (k+1, road)))

