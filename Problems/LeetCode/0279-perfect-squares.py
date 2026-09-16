class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def solve(n):
            if n==0:
                return 0
            if n<0:
                return float("inf")
                
            mini = n
            
            i = 1
            while i*i<=n:
                mini = min(mini, solve(n-(i*i)))
                i+=1
                
            return mini+1

        return solve(n)