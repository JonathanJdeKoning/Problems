class Solution:
    def minimumFlips(self, n: int) -> int:
        b = bin(n)[2:]
        r = b[::-1]
        return sum(1 for x,y in zip(b,r) if x!= y)