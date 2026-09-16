class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            nums = [(a+b)%10 for a,b in pairwise(nums)]
        return nums[0]