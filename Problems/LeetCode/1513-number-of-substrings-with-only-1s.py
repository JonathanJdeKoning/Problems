class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        for k, v in groupby(s):
            v = list(v)
            if v[0] == "1":
                n = len(v)
                ans += (n*(n+1))//2
        return ans%1000000007