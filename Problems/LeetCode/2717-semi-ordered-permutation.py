class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        last =len(nums)-1
        total = 0
        mindex = nums.index(1)
        maxdex = nums.index(len(nums))
        if mindex>maxdex:
            total -=1
        total += mindex
        total += last-maxdex
        return total
