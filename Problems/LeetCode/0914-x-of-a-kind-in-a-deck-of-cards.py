class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
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
            return factors
        
        count = Counter(deck)
        check = []
        if 1 in count.values(): return False
        for c in count.values():
            check.append(set(prime_factors(c)))
        return len(set.intersection(*check)) != 0

