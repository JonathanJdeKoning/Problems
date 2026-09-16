
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]*(high+1)
        dp[zero] += 1
        dp[one] += 1
        ans = 0
        for i in range(min(zero, one), high+1):
            dp[i] += (dp[i-zero] + dp[i-one])%1000000007
            if i >= low and i <= high:
                ans += dp[i]
        
        return ans%1000000007

        