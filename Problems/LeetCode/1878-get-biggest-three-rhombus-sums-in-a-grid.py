class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        best = []
        R, C = len(grid), len(grid[0])
        def rhombsAt(i,j):
            rhombs = [grid[i][j]]
            dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]
            dist = 1
            while i+dist < R and j+dist < C and i-dist >=0 and j-dist >=0 :
                tot = 0
                
                points = [(i-dist, j), (i, j+dist), (i+dist,j), (i,j-dist)]
                
                for (dy, dx), (y,x) in zip(dirs, points):
                    dowhile = True
                    while dowhile or (y, x) not in points:
                        dowhile = False
                        tot += grid[y][x]
                        y += dy
                        x += dx
                rhombs.append(tot)
                dist += 1


            return rhombs

            

        for i in range(R):
            for j in range(C):
                rhombs = rhombsAt(i,j)
                for rhomb in rhombs:
                    if rhomb in best: continue
                    heappush(best, rhomb)
                    while len(best) > 3:
                        heappop(best)

        return sorted(best, reverse=True)
