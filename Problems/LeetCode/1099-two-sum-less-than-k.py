class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                arr.append(nums[i] + nums[j])
        mx = -1

        for num in arr:
            if num < k:
                mx = max(mx, num)
        return mx