class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        n = len(nums)
        c = (r - l) + 1
        return c > n / 2