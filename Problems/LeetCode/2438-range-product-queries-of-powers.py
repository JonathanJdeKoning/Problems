from operator import __mul__
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = int(1e9+7)
        b = bin(n)[2:][::-1]
        nums = []

        for i in range(len(b)):
            if b[i] == "1":
                nums.append(2**i)
        
        ans = []
        @cache
        def voila(s,e):
            return reduce(__mul__, nums[s:e+1]) % mod
        for s, e in queries:
            ans.append(voila(s, e))
        return ans