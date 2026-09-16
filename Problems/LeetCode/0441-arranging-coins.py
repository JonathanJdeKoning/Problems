class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        currrow = 2
        while True:
            start += currrow
            currrow += 1
            if start > n:
                return currrow-2
            
        