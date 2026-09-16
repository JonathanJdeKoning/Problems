class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums) | set([int(str(x)[::-1]) for x in nums]))

