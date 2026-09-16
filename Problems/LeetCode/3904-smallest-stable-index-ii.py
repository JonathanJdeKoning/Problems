class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:        
        mins = [None]*len(nums)
        mn = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            mn = min(mn, nums[i])
            mins[i] = mn

        mx = nums[0]
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            stable = mx - mins[i] <= k
            if stable: return i
        print(mins)
        return -1
