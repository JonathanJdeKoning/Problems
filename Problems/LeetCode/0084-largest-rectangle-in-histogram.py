class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        ans = 0
        heights.append(0)
        for i, h in enumerate(heights):

            if not stack or (h >= stack[-1][-1]):
                stack.append((i, h))
                continue
            
            while stack and stack[-1][-1] > h:
                pi, ph = stack.pop()
                ans = max(ans, ph * (i - pi))
            stack.append((pi, h))

        return ans
                
            