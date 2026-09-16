class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        tot = 0
        for k,v in groupby(nums):
            if k != 0: continue

            n = len(list(v))
            tot += (n*(n+1))//2
            
        return tot