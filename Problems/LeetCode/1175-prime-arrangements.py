class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 2: return 1
        def fact(n):
            total = 1
            while n != 0:
                total *= n
                n-=1
            return total

        def prime(x):
            prime_list = []
            for i in range(x+1):
                if i == 0 or i == 1:
                    continue
                else:
                    for j in range(2, int(i/2)+1):
                        if i % j == 0:
                            break
                    else:
                        prime_list.append(i)
            return len(prime_list)
        return((fact(n - prime(n))*fact(prime(n)))%(10**9+7))