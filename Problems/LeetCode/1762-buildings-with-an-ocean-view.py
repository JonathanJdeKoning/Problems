class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        mx = 0
        ans = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if h > mx:
                ans.append(i)
            mx = max(mx, h)
        return ans[::-1]