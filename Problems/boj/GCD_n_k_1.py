
from math import gcd
from functools import reduce
from math import isqrt
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def is_prime(n):
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
def get_phi(n):
    result = n
    p = 2
    # Iterate only up to sqrt(n)
    while p * p <= n:
        if n % p == 0:
            # p is a prime factor.
            # Apply formula: result = result * (1 - 1/p)
            # Which simplifies to: result -= result // p
            result -= result // p
            
            # Divide n by p repeatedly to remove this factor entirely
            while n % p == 0:
                n //= p
        p += 1
        
    # If n > 1 remaining, it is a prime factor itself
    if n > 1:
        result -= result // n
        
    return result


def sol(N):

    P = [f for f in factors(N) if is_prime(f)]
    ans = N

    for x in P:
        ans -= N//x
    for i in range(len(P)-1):
        for j in range(i+1, len(P)):
            ans += N//(P[i]*P[j])

    for i in range(len(P)-2):
        for j in range(i+1, len(P)-1):
            for k in range(j+1, len(P)):
                ans -= N//(P[i]*P[j]*P[k])

    for i in range(len(P)-3):
        for j in range(i+1, len(P)-2):
            for k in range(j+1, len(P)-1):
                for l in range(k+1, len(P)):
                    ans += N//(P[i]*P[j]*P[k]*P[l])
    
    for i in range(len(P)-4):
        for j in range(i+1, len(P)-3):
            for k in range(j+1, len(P)-2):
                for l in range(k+1, len(P)-1):
                    for m in range(l+1, len(P)):
                        ans -= N//(P[i]*P[j]*P[k]*P[l]*P[m])
    
    for i in range(len(P)-5):
        for j in range(i+1, len(P)-4):
            for k in range(j+1, len(P)-3):
                for l in range(k+1, len(P)-2):
                    for m in range(l+1, len(P)-1):
                        for n in range(m+1, len(P)):
                            ans += N//(P[i]*P[j]*P[k]*P[l]*P[m]*P[n])

    for i in range(len(P)-6):
        for j in range(i+1, len(P)-5):
            for k in range(j+1, len(P)-4):
                for l in range(k+1, len(P)-3):
                    for m in range(l+1, len(P)-2):
                        for n in range(m+1, len(P)-1):
                            for o in range(n+1, len(P)):
                                ans -= N//(P[i]*P[j]*P[k]*P[l]*P[m]*P[n]*P[o])
    for i in range(len(P)-7):
        for j in range(i+1, len(P)-6):
            for k in range(j+1, len(P)-5):
                for l in range(k+1, len(P)-4):
                    for m in range(l+1, len(P)-3):
                        for n in range(m+1, len(P)-2):
                            for o in range(n+1, len(P)-1):
                                for p in range(n+1, len(P)):
                                    ans += N//(P[i]*P[j]*P[k]*P[l]*P[m]*P[n]*P[o]*P[p])


    return ans

N = int(input())
print(sol(N), get_phi(N))
