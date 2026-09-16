from math import gcd
ans = 0

for D in range(1, 12001):
    for N in range(D//3, D//2+2):
        if gcd(D, N) != 1: continue
        F = N/D
        if F <= 1/3: continue
        if F >= 1/2: continue
        ans += 1

print(ans)
