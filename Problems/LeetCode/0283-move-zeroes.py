class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZero = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
                lastNonZero += 1
        