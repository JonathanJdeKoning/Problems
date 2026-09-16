class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    cnt += 1
                
                if cnt > (j-i+1)/2:
                    ans += 1
        return ans