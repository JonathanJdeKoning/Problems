class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:


        drunk = 0
        emptyBottles = 0
        while True:
            drunkThisRound = numBottles
            numBottles = 0
            drunk += drunkThisRound
            emptyBottles += drunkThisRound

            if (emptyBottles // numExchange) > 0:
                while (emptyBottles // numExchange) > 0:
                    emptyBottles -= numExchange
                    numBottles += 1
                    numExchange += 1
                continue
            else:
                return drunk
                break
                
            