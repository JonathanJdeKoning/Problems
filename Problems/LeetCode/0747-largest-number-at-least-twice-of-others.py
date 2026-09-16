class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s = sorted(nums)
        if s[-1] >= s[-2]*2:
            return nums.index(max(nums))
        return -1