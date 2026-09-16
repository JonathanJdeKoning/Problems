class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = nums[::-1]
        ans = 0
        while True:
            if len(set(nums)) == len(nums):
                return ans
            try:
                nums.pop()
            except: pass
            try:
                nums.pop()
            except: pass
            try:
                nums.pop()
            except: pass
            ans += 1