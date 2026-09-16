class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementsum = sum(nums)
        nums = [str(num) for num in nums]
        digitsum = 0
        for num in nums:
            for c in num:
                digitsum += int(c)
        return abs(digitsum - elementsum)