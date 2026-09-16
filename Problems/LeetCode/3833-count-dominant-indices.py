class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            total = 0
            for j in range(i+1, len(nums)):
                total += nums[j]
            if nums[i] > total / (len(nums) - i - 1):
                ans += 1
        return ans