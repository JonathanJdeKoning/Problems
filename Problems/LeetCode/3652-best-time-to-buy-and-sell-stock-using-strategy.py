class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        base = sum([prices[i] * strategy[i] for i in range(len(prices))])
        ans = base

        l = 0
        m = k//2
        r = k

        for i in range(l, m):
            if strategy[i] == 1:
                base -= prices[i]
            elif strategy[i] == -1:
                base += prices[i]
        for i in range(m, r):
            if strategy[i] == 0:
                base += prices[i]
            elif strategy[i] == -1:
                base += prices[i] * 2
        ans = max(ans, base)
        #print(ans)
        while True:
            #print(l, m, r)
            if r == len(prices): break
            
            if strategy[r] == 0:
                base += prices[r]
            elif strategy[r] == -1:
                base += prices[r] * 2

            r += 1

            if strategy[l] == -1:
                base -= prices[l]
            elif strategy[l] == 1:
                base += prices[l]

            l += 1


            base -= prices[m]

            m += 1
            ans = max(ans, base)
        return ans