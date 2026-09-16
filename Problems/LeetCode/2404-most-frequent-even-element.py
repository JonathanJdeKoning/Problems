class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mynums = defaultdict(int)
        good = False
        for num in nums:
            if num%2==0: 
                mynums[num]+= 1
                good = True
        if not good: return -1
        new = list(mynums.items())
        print(new)
        mx = 0
        out = None
        for tup in new:
            if tup[1] == mx:
                out = min(tup[0], out)
            elif tup[1] > mx:
                out = tup[0]
                mx = tup[1]
        return out
