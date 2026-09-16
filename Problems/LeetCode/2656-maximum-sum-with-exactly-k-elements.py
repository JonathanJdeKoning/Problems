class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(k):
            total += max(nums)+i
        return total