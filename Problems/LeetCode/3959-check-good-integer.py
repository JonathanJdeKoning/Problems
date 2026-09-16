class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digs = [int(c) for c in str(n)]
        digitSum = sum(digs)
        squareSum = sum([x**2 for x in digs])
        return squareSum - digitSum >= 50