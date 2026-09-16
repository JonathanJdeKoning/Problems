class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mx = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i>=j or j>=k or i>= k: continue
                    mx = max(mx, (nums[i]-nums[j])*nums[k])
        if mx >=0: return mx
        return 0
