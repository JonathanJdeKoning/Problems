class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        suff = [0]*(N+1)
        for l,r in queries:
            suff[l] += 1
            suff[r+1] -= 1

        prefix = list(accumulate(suff))
        return all([nums[i] - prefix[i] <= 0 for i in range(N)])
        
