class Solution:
    def isUgly(self, n: int) -> bool:
        def prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return list(set(factors))
        if n <=0: return False
        primes = prime_factors(n)

        return len([x for x in primes if x != 2 and x!= 3 and x!=5]) ==0