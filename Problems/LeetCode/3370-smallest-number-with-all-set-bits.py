class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n
        while True:
            if x.bit_count() == len(bin(x)[2:]):
                return x
            x += 1