class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for currStart, currEnd in intervals[1:]:
            prevEnd = ans[-1][-1]
            # If overlap
            if currStart <= prevEnd:
                ans[-1][-1] = max(currEnd, prevEnd)
            else:
                ans.append([currStart, currEnd])

        return ans

        