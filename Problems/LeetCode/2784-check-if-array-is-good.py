class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if not len(nums) == max(nums)+1: return False
        if not nums.count(max(nums))==2: return False
        return list(Counter(nums).values()).count(1) == len(nums)-2