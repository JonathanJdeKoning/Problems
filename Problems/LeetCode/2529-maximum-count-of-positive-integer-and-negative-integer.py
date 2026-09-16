class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        numNeg = bisect_left(nums, 0)
        numPos = len(nums) - bisect_right(nums, 0)

        return max(numNeg, numPos)