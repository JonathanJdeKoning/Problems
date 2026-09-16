class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r = 1
        curr = 1
        while True:
            #print(f"{l=} {r=}")
            if r == len(prices): 
                ans += (curr*(curr+1))//2
                break
            if prices[r] == prices[l] - curr:
                curr += 1
            else:
                ans += (curr*(curr+1))//2
                l = r
                curr = 1
            
            r += 1
        return ans

