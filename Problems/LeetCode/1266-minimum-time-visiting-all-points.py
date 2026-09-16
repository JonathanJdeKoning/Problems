class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        starty,startx = points[0]
        for pointy,pointx in points[1:]:            
            ydiff = abs(starty-pointy)
            xdiff = abs(startx-pointx)
            total += max(ydiff, xdiff)
            starty,startx = pointy,pointx
        return total
            
