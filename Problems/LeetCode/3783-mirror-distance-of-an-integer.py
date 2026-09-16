class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror = 0

        x = n
        mirror = 0
        while x:
            x, r = divmod(x, 10)
            mirror *= 10
            mirror += r

        return abs(mirror - n)  