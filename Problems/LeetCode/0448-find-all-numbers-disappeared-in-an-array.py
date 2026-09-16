class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        oth = set(range(1, len(nums)+1))
        nums = set(nums)
        return list(oth-nums)