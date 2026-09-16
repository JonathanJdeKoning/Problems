class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = [0]*1001
        b = [0]*1001

        for x in target:
            a[x]+=1
        for x in arr:
            b[x]+=1
        return a==b