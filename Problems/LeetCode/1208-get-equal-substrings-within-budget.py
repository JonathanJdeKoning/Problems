class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        l = 0
        r = 0
        ans = 0
        tot = cost[l]
        while True:
            if r==len(s): break

            slc = cost[l:r+1]
            if sum(slc) <= maxCost:
                ans = max(ans, len(slc))
                r+=1
            else:
                l+=1
                r+=1
        return ans
