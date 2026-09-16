class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        for i in range(len(nums)-1):
            mx = max(mx, nums[i+1]-nums[i])
        return mx
            