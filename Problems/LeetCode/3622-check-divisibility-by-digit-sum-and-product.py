class Solution:
    def checkDivisibility(self, n: int) -> bool:
        D = [int(x) for x in str(n)]
        s = sum(D)
        p = reduce(lambda x, y:x*y, D)
        return n%(s+p)==0