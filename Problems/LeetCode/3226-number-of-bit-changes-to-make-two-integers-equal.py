class Solution:
    def minChanges(self, n: int, k: int) -> int:
        a = bin(n)[2:].zfill(25)
        b = bin(k)[2:].zfill(25)
        total = 0
        for x,y in zip(a,b):
            if x=="1" and y=="0":
                total += 1
            elif x=="0" and y=="1":
                return -1
        return total