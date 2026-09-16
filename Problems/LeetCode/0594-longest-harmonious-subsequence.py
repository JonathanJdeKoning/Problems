class Solution:
    def findLHS(self, nums: List[int]) -> int:
        new = [(k,len(list(v))) for k,v in groupby(sorted(nums))]
        mx = 0
        for i in range(len(new)-1):
            a = new[i]
            b = new[i+1]
            if b[0] != a[0]+1: continue
            mx = max(mx, a[1]+b[1])
        return mx

        