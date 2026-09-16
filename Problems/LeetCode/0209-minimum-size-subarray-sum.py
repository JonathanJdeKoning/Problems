class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        l = 0
        r = 1
        tot = nums[l]
        ans = inf
        while r <= len(nums):
            while tot >= target:
                ans = min(ans, r-l)
                tot -= nums[l]
                l += 1
            if r == len(nums): break
            tot += nums[r]
            r += 1
        return ans

