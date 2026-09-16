class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        n = min(nums)
        digsum = sum(int(x) for x in str(n))
        if digsum % 2 ==0:
            return 1
        else:
            return 0