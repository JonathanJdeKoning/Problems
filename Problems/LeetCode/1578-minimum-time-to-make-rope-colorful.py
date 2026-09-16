class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0 
        for k, v in groupby(zip(colors, neededTime), key = lambda x: x[0]):
            v = list(v)
            if len(v) == 1: continue
            times = [x[1] for x in v]
            ans += sum(times) - max(times)
        return ans