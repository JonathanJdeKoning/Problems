class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        tot = prices[0] + prices[1]
        if tot<=money:
            return money-tot
        return money
