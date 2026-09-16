class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1, 400):
            if k*i not in nums: return k*i