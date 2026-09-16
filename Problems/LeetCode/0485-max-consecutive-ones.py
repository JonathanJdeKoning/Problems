class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx, curr = 0, 0
        for n in nums:
            if n == 1: curr += 1; continue
            mx = max(curr, mx); curr = 0
        return max(curr, mx)