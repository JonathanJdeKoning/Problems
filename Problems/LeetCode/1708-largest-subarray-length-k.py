class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return [max(nums)]
        mx = max(nums[:-(k-1)])
        idx = nums.index(mx)
        return nums[idx:idx+k]