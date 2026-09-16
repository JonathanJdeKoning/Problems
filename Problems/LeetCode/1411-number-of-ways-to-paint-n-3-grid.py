class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = int(1e9)+7
        @cache
        def f(n):
            if n == 0: return 2
            if n == 1: return 9
            return (5 * f(n-1) - 2*f(n-2))%MOD
        return (f(n-1)*6)%MOD
