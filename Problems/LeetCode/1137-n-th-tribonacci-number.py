class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def trib(n): return int(n > 0) if n < 3 else trib(n-1)+trib(n-2)+trib(n-3)
        return trib(n)