class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digs = [int(x) for x in str(n)]
        return functools.reduce(lambda x,y: x*y, digs)-sum(digs)