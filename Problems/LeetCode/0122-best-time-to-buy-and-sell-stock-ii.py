class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for a,b in pairwise(prices):
            ans += max(0,b - a )
        return ans
