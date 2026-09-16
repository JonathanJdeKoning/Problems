class Solution:
    def minEnd(self, n: int, x: int) -> int:
        mn = (["0"]*50 + list(bin(x))[2:])[::-1]
        fill = list(bin(n-1)[2:])[::-1]
        
        currcell = 0        
        for i, mncell in enumerate(mn):
            if mncell == "1": continue
            mn[i] = fill[currcell]
            currcell+=1
            if currcell == len(fill): break
        return int("".join(mn)[::-1],2)
                