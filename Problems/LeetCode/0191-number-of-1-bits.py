class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n))[2:].count("1")