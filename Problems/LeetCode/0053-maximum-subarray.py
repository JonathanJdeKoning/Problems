class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            grow = prev + nums[i]
            restart = nums[i]

            prev = max(grow, restart)
            ans = max(ans, prev)

        return ans


   


