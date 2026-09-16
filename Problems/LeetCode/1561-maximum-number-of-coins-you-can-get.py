class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum(piles[1:len(piles)- len(piles)//3:2])