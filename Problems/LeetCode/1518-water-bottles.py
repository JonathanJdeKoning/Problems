class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drank = empty

        while True:
            newbottles = empty//numExchange
            if newbottles == 0:
                break
            empty -= newbottles*numExchange
            empty += newbottles
            drank += newbottles
        return drank


