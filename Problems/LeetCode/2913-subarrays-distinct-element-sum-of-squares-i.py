class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                slc = nums[i:j]
                total += len(set(slc))**2
        return total