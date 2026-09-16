class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        perm = copy.copy(nums)
        p = 0
        n = 0
        while p < len(nums):
            if perm[p] > nums[n]:
                n += 1
            p += 1 
        return n