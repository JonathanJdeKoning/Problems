class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i, num in enumerate(nums, start = 1):
            if n%i==0:
                total += num**2
        return total