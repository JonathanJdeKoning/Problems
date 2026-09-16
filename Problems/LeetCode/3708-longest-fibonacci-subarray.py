class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        dp = [2]*len(nums)
        dp[0] = 1
        for i in range(2, len(nums)):
            if nums[i-1] + nums[i-2] == nums[i]:
                dp[i] = dp[i-1] + 1
        return max(dp)