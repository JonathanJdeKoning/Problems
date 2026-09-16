class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        t2n = lambda t:int(t.replace(":",""))
        time = sorted([tuple(map(t2n, event1)), tuple(map(t2n, event2))])
        return time[1][0] <= time[0][1]
