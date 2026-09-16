class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -inf
        for i, c in enumerate(nums):
            if c == 0: continue
            if i-last <= k: return False
            last = i
        return True