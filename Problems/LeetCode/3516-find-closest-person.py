class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) < abs(z-y):
            return 1
        elif abs(z-y) < abs(z-x):
            return 2
        return 0