class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        mn = nums.index(min(nums))
        mx = nums.index(max(nums))
        mn, mx = sorted([mn, mx])

        l = mx+1
        r = N - mn
        m = mn+1 + (N-mx)
        return min(l,m,r)