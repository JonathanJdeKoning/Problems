class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        @cache
        def numWaysStartingAt_StartingWith_(i, curr):
            if i >= len(nums): return 0
            if i == len(nums) - 1:
                a = curr - nums[i] == target
                b = curr + nums[i] == target
                return a+b

            return numWaysStartingAt_StartingWith_(i+1,curr+nums[i]) + numWaysStartingAt_StartingWith_(i+1,curr-nums[i])
        return numWaysStartingAt_StartingWith_(0, 0)