class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new = sorted(nums, reverse=True)
        good = new[:k]

        out = []
        for num in nums:
            if num in good:
                out.append(num)
                good.remove(num)
        return out