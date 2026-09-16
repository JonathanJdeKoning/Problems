class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 1000000):
            digprod = reduce(lambda x,y: x*y, [int(z) for z in str(i)])
            if digprod%t==0: return i