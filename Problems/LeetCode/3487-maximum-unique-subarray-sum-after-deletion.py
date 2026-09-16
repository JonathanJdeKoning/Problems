class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos = [x for x in list(set(nums)) if x > 0]
        if not pos: return max(nums)
        return sum(pos)