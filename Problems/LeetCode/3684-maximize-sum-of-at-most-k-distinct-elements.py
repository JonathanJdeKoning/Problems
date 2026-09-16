class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(set(nums))
        ans = []
        for _ in range(k):
            if nums:
                ans.append(nums.pop())
        return ans