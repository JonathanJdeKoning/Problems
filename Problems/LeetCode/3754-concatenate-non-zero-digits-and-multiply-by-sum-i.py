class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0
        digsum = sum([int(x) for x in str(n)])
        x = int("".join([c for c in str(n) if c != "0"]))
        return x * digsum