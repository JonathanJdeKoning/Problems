class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, int(1e9)):
            s = str(i)
            fq = Counter(s)
            if all([int(k) == v for k,v in fq.items()]):
                return i