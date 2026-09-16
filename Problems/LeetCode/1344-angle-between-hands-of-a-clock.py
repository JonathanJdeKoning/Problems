class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        minAng = minutes * 6
        if minAng == 0: minAng = 360

        hourAng = 30*hour
        
        if minAng != 360 and minAng != 0:hourAng +=  30 / (360/minAng)

        ans =  min(abs(hourAng-minAng), 360 - abs(hourAng-minAng))
        if ans ==360: ans = 0
        return ans