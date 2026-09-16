class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        maxA = total//cost1
        for i in range(maxA+1):
            t = total - cost1*i
            ans += t//cost2 + 1
        return ans
