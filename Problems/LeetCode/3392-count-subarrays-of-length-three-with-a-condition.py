class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            slc = nums[i:i+3]
            if float((slc[0] + slc[2])) == slc[1] /2 :
                ans += 1
        return ans