class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf]*len(nums)
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(1,num+1):
                if i+j == len(nums):break
                dp[j+i] = min(dp[j+i],dp[i]+1)
        return(dp[-1])