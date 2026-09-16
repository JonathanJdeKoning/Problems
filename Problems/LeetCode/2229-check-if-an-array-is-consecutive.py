class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for a,b in pairwise(nums):
            if b != a+1: return False
        return True