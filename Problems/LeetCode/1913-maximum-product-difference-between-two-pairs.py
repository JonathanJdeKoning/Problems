class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a= max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        c = min(nums)
        nums.remove(c)
        d = min(nums)
        return a*b-c*d