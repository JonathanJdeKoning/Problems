class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+2)
        memo[1] = 1
        memo[2] = 2

        def distinctWays(n):
            if memo[n] != -1:
                return memo[n]
            ans = distinctWays(n-1) + distinctWays(n-2)
            memo[n] = ans
            return ans

        return distinctWays(n)