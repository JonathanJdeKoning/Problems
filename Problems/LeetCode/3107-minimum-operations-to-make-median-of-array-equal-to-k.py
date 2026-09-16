class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            if (i < n // 2): 
                ans += max(0, nums[i] - k)
            elif (i == n // 2): 
                ans += abs(k - nums[i]) 
            else:
                ans += max(0, k - nums[i]); 

        return ans
            
            