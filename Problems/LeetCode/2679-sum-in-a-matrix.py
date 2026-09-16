class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        for i in range(len(nums)):
            nums[i] = sorted(nums[i])

        for i in range(len(nums[0])):
            ans += max([row[i] for row in nums])
        return ans