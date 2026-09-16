class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l,r+1, k):
                nums[i] =  (nums[i] * v) % int(1e9 + 7)
        base = 0
        for num in nums:
            base ^= num
        return base 
                