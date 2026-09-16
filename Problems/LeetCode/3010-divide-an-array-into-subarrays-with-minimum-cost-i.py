class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        nums = nums[1:]
        b = min(nums)
        bx = nums.index(b)
        c = min(nums[:bx]+nums[bx+1:])
        return a+b+c