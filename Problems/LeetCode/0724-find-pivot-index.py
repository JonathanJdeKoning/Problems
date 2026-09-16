class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        count = 0
        for i, num in enumerate(nums):
            count += num
            if (count-num) == (tot-num)/2:
                return i
        return -1