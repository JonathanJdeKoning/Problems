class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[0] - nums[-1]), max(abs(a-b) for a,b in pairwise(nums)))