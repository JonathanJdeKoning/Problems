class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        fq = Counter({i:0 for i in range(value)})
        fq.update(Counter([num % value for num in nums]))
        mnLoops = min(list(fq.values()))
        mnMod = min([k for k in fq if fq[k] == mnLoops])
        return value*mnLoops + mnMod