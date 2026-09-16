class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        f = sorted(factors(n))
        if k > len(f): return -1
        return f[k-1]