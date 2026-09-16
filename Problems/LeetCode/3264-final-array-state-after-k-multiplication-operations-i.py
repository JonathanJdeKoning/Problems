class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mn = min(nums)
            for i, num in enumerate(nums):
                if num == mn:
                    nums[i]*=multiplier
                    break

        return nums
                