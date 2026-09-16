class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out = []
        for i, obj in enumerate(prices):
            disc = False
            for j, price in enumerate(prices[i+1:], start = i+1):
                if price <= obj:
                    out.append(obj-price)
                    disc = True
                    break
            if not disc:
                out.append(obj)
        return out
