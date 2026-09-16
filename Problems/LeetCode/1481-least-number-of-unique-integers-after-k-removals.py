class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        fq = Counter(arr)
        val = sorted(fq.values(), reverse=True)
        while val and k >= val[-1]:
            k -= val.pop()    
        return len(val)

