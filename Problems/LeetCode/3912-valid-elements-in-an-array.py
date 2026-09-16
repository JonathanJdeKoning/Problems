class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        return [x for i, x in enumerate(nums) if x > max(nums[:i], default=0) or x > max(nums[i+1:],default=0)]