class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        fq = Counter(nums)
        degree = max(fq.values())
        ans = inf
        for poss in [k for k,v in fq.items() if v == degree]:
            start = nums.index(poss)
            end = len(nums) - nums[::-1].index(poss) 
            ans = min(ans, end-start)
        return ans