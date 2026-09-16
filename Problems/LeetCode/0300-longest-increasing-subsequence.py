class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        for i, num in enumerate(nums[1:], start=1):
            for j, res in enumerate(dp[:i]):
                if num > nums[j]:
                    dp[i] = max(dp[i], res+1)

        return(max(dp))
