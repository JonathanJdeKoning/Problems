class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if not (1 in nums and 2 in nums): return -1

        x = [i for i in range(len(nums)) if nums[i] == 1]
        y = [i for i in range(len(nums)) if nums[i] == 2]
        return min([abs(a-b) for a in x for b in y])