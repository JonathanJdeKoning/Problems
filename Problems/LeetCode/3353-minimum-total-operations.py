class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return len(list(groupby(nums))) - 1