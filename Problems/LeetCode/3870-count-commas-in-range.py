class Solution:
    def countCommas(self, n: int) -> int:
        def c(n):
            n = len(str(n))
            n -= 3
            return ceil(n/3)
        ans = 0
        for i in range(1000, n+1):
            ans += c(i)
        return ans