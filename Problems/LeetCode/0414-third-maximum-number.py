class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mx1 = max(nums)
        while nums.count(mx1) > 0:
            nums.remove(mx1)
        try:
            mx2 = max(nums)
        except: return mx1
        while nums.count(mx2) > 0:
            nums.remove(mx2)
        try:
            return max(nums)
        except:
            return max(mx1, mx2)