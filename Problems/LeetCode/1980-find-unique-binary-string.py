class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        nums = set(nums)

        for i in range(2**n):
            b = bin(i)[2:].zfill(n)
            if b not in nums:
                return b