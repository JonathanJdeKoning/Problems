class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        redEves = 0
        blueEves = 0
        blueOdds = 0
        redOdds = 0
        tempred = red
        tempblue = blue
        for i in range(1,51,2):
            if tempred >= i:
                tempred -= i
                redOdds+=1
            if tempblue >= i:
                tempblue -= i
                blueOdds+=1
        tempred = red
        tempblue = blue
        for i in range(2,51,2):
            if tempred >= i:
                tempred -= i
                redEves+=1
            if tempblue >= i:
                tempblue -= i
                blueEves+=1
                
        if blueOdds > redEves:
            blueOdds = redEves+1
        if redOdds > blueEves:
            redOdds = blueEves+1
        
        if redEves > blueOdds:
            redEves = blueOdds
        if blueEves > redOdds:
            blueEves = redOdds
        return max(blueEves+redOdds, redEves+blueOdds)
            