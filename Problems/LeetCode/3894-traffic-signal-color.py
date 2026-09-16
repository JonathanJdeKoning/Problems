class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0: return "Green"
        if timer == 30: return "Orange"
        if timer <= 90 and timer >= 31: return "Red"
        return "Invalid"