class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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
        return out

            
            