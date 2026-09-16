class Solution:
    def removeZeros(self, n: int) -> int:
        return int("".join([x for x in str(n) if x != "0"]))