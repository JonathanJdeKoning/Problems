
from math import sqrt
def x(b):
    return (sqrt(8*b**2 - 8*b + 1)+1)/2 

"""
low = 100 #bad
high = 10**12 #good

while high > low+1:
    mid = (high+low)//2
    if x(mid) > 10**12:
        high = mid
    else:
        low = mid
"""
#for i in range(1, 10000000000):
#    if x(i).is_integer():
#        print(i)
print(x(756872327473))
i
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

