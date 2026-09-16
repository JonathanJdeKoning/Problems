class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        intervals = meetings
        intervals.sort()
        out = []
        curr = intervals[0]
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if start > curr[1]:
                out.append(curr)
                curr = interval
            else:
                curr[1] = max(end, curr[1])
        out.append(curr)
        for s, e in out:
            days -= (e-s)+1
        return days
