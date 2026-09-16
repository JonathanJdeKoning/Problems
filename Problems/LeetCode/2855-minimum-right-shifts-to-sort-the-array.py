class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        mn = min(nums)
        mndx = nums.index(mn)
        if nums[mndx:] + nums[:mndx] != sorted(nums): return -1
        if mndx == 0: return 0
        return len(nums) - mndx