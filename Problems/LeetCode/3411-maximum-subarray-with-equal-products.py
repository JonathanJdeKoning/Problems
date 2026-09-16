from operator import __mul__
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                chk = nums[i:j]
                p = reduce(__mul__, chk)
                l = reduce(lcm, chk)
                g = reduce(gcd, chk)
                if p == l * g:
                    ans = max(ans, j-i)
        return ans