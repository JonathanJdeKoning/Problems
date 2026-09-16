class Solution:
    def rob(self, nums: List[int]) -> int:
        A = nums[0:-1]
        B = nums[1:]
        ans = nums[0]
        a, b = 0,0
        for num in A:
            a, b = max(b+num,a), a

        ans = max(ans, a)
        a, b = 0,0
        for num in B:
            a, b = max(b+num,a), a
        ans = max(ans, a)
        return ans