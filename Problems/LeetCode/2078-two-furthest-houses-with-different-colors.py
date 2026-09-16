class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        loc = {} 
        for i, c in enumerate(colors):
            if c not in loc:
                loc[c] = [i,i]
            else:
                low, high = loc[c]
                loc[c] = [min(low, i), max(high, i)]

        v = list(loc.values())

        ans = 1
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                x,y = v[i]
                a,b= v[j]
                ans = max(ans, max(abs(x-b), abs(a-y)))
        return ans