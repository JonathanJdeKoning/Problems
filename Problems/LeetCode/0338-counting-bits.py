class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(x).count("1") for x in range(n+1)]