class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        def strict(nums):
            p = list(pairwise(nums))
            return all([a<b for a,b in p]) or all([a>b for a,b in p])
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if strict(nums[i:j]):
                    ans = max(ans, j-i)
        return ans
