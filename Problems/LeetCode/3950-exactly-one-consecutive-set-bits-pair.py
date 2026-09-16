class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b = bin(n)[2:]
        return b.count("11") == 1 and b.count("111") == 0