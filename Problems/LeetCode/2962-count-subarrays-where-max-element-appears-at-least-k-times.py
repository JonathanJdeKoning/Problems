class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == mx:
                k -= 1

            right+=1
            
            while k == 0:
                if nums[left] == mx:
                    k += 1
                left+=1
                
            ans += left
        return ans