class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join(["1" if x == "0" else "0" for x in bin(n)[2:]]), 2)