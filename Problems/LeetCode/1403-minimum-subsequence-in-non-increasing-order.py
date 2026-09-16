class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)
        total = sum(nums)
        out = []
        x = 0
        for num in nums:
            total -= num
            x += num
            out.append(num)
            if x > total: break
        return out