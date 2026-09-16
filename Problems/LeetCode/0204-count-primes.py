class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        sieve = [False]*n
        sieve[0] = True
        sieve[1] = True
        total = -2
        for i, num in enumerate(sieve):
            if not num:
                for j in range(i+i, n, i):
                    if not sieve[j]:
                        sieve[j] = True
                        total += 1

        return sieve.count(False)
