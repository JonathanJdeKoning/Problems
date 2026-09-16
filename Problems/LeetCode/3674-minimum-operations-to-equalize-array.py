class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return int(not(len(set(nums)) == 1))