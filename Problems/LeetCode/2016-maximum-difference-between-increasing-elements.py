class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i >= j: continue
                if nums[i] >= nums[j]: continue
                mn = max(mn, nums[j] - nums[i])
        return mn