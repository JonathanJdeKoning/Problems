class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans = -1
        tx, ty = target
        bestDist = inf
        for i, (dx, dy, r) in enumerate(drones):
            dist = abs(dx - tx) + abs(dy - ty)
            if dist <= r and dist < bestDist:
                bestDist = dist
                ans = i
        return ans
