class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxProfit = 0
        mnPrice = prices[0]
        for price in prices:
            profit = price - mnPrice
            mxProfit = max(mxProfit, profit)
            mnPrice = min(mnPrice, price)
        return mxProfit