from functools import cache
from itertools import permutations, combinations
@cache
def isPrime(n):
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

@cache
def concat(x, y):
    return int(str(x)+str(y))

@cache
def primeConcats(x,y):
    return isPrime(concat(x,y)) and isPrime(concat(y, x))

def validAdd(new, primes):
    return all(primeConcats(new, p) for p in primes)

MX = 12
P = [3,5,7,11]


#LUCKY THAT FIRST ONE FOUND IS SMALLEST, NOT GUARANTEED
def solve(primes, left):
    if left == 0: exit(print(sum(primes)))
    
    for p in P:
        if p in primes: continue
        if not validAdd(p, primes): continue

        solve(primes | {p}, left-1)

    
cardinality = 5
while True:
    MX += 1
    if not isPrime(MX): continue
    solve({MX}, cardinality-1)
    P.append(MX)
