class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        out = []
        base = sum([x for x in nums if x%2==0])
        for val, idx in queries:
            oldnum = nums[idx]
            newnum = oldnum+val
            nums[idx] += val
            if oldnum%2==0: base -= oldnum
            if newnum%2==0: base +=newnum
            out.append(base)
        return out            