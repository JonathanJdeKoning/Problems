class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        bad = set()

        for i in range(len(intervals)-1):
            aS, aE = intervals[i]
            for j in range(i+1, len(intervals)):
                bS, bE = intervals[j]

                if aS >= bS and aE <= bE:
                    bad.add(i)

                if bS >= aS and bE <= aE:
                    bad.add(j)
        return len(intervals) - len(bad)