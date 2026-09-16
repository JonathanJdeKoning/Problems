class Solution:
    def alternateDigitSum(self, n: int) -> int:
        tot = 0
        for i,c in enumerate(str(n)):
            if i%2 == 0: tot += int(c)
            else:
                tot -= int(c)
        return tot