class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for i, c in enumerate(nums):
            n = (c+i)%len(nums)
            res.append(nums[n])
        return res