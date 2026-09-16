class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans