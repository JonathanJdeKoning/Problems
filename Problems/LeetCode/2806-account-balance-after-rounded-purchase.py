class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100-10*round((purchaseAmount+0.1)/10)