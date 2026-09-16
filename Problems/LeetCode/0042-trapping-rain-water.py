class Solution:
    def trap(self, height: List[int]) -> int:  
        total = 0

        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax <= rightMax:
                total += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                total += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        return total