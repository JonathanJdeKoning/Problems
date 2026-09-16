from itertools import accumulate
def prime_sieve(n):
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend([3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1])
    return res

MXP = 4_000_000
P = prime_list(MXP)
pref = list(accumulate(P,initial=0))

ans = 0
l = 0
r = 0
N = int(input())
while True:
    if l not in range(len(pref)): break
    if r+1 not in range(len(pref)): break
    n = pref[r+1] - pref[l]
    if n == N:
        ans += 1
        l += 1
        continue
    if n < N:
        r += 1
        continue
    if n > N:
        l += 1
        continue
print(ans)