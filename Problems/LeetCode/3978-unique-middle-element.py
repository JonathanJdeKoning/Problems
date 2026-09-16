class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        fq = Counter(nums)
        m = nums[len(nums)//2]
        return fq[m] == 1