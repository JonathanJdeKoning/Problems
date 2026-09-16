class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        t = max(nums) - min(nums)
        return t * k