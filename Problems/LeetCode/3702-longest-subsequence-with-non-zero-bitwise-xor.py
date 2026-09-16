class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all([x==0 for x in nums]): return 0
        base = reduce(lambda x,y: x^y, nums)
        if base != 0: return len(nums)
        return len(nums) - 1