class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        l =0 
        r = len(height)-1
        while l<r:
            left = height[l]
            right = height[r]
            ans = (r-l)*min(right, left)
            mx = max(ans, mx)

            if left < right:
                l += 1
            elif right <= left:
                r -= 1 
            
        return mx