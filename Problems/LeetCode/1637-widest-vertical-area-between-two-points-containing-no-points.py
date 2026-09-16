class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs= sorted([x[0] for x in points])
        mx = 0
        for i in range(len(xs)-1):
            mx = max(mx, abs(xs[i]-xs[i+1]))
        return mx