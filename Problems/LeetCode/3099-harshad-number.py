class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digsum  = sum([int(d) for d in str(x)])
        if x % digsum ==0:
            return digsum
        return -1