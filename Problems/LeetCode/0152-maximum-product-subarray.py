class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def prod(i):
            nonlocal nums
            n = nums[i]
            if n == 0: return (0,0)
            if i == 0: return (n,n)

            mnPrev, mxPrev = prod(i-1)

            return (min(n*mnPrev, n*mxPrev, n), max(n*mnPrev, n*mxPrev, n))

        return max([prod(i)[1] for i in range(len(nums))])

            
