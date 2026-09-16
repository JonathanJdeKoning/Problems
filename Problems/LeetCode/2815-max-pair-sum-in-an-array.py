class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j >= i: continue
                if max([int(x) for x in str(nums[i])]) == max([int(x) for x in str(nums[j])]):
                    mx = max(nums[i]+nums[j],mx)
        return mx