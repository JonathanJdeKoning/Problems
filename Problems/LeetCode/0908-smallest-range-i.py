class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        if nums[0] + k >= nums[-1] -k: return 0
        return (nums[-1]-k)-(nums[0]+k)