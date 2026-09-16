class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))

        tot = 0

        for num in str(n):
            tot += int(num) ** k
        return tot == n