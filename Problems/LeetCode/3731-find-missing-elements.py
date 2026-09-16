class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        N = max(nums)
        return sorted(set(range(min(nums), N+1)) - set(nums))