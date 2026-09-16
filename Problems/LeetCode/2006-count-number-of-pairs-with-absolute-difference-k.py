class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j>= i: continue
                if abs(nums[i]-nums[j]) == k: total += 1
        return total