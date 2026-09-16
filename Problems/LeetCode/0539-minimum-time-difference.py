class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def minutes(s):
            h, m = s.split(":")
            return int(h)*60 + int(m)

        timePoints.sort(key=minutes)
        timePoints.append(timePoints[0])
        print(timePoints)
        ans = inf
        for a,b in pairwise(timePoints):
            reg = abs(minutes(b) - minutes(a))
            loop = abs(minutes("24:00") - minutes(a) + minutes(b))
            ans = min(ans, reg)
            ans = min(ans, loop)
        return ans