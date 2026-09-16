class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any([Counter(list(str(2**i))) == Counter(list(str(n))) for i in range(31)])