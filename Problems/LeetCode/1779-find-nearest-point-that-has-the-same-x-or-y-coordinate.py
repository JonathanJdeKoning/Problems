class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mn = math.inf
        out = -1
        for i, point in enumerate(points):
            if point[0] != x and point[1] != y: continue

            dist = abs(x-point[0])+ abs(y-point[1])
            if dist < mn:
                mn = dist
                out = i
        return out
