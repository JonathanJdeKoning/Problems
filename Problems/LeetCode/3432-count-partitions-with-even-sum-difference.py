class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans =0 
        for i in range(len(nums)-1):
            left = nums[:i+1]
            right = nums[i+1:]
            if (sum(left) - sum(right))%2==0:
                ans += 1
        return ans