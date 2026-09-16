class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xs = sorted([x[0] for x in points])
        tot = 1
        good = xs[0]+w
        for x in xs:
            if x <= good:
                continue
            else:
                tot += 1
                good = x+w
        return tot
            
            