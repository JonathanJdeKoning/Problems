from collections import defaultdict
from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = int(input())
A = list(map(int, input().split()))
mp = defaultdict(int)
mx = 0
for num in A:
    f = factors(num)
    f.discard(1)

    for ff in f:
        mp[ff] += 1
        mx = max(mx, mp[ff])

for k in mp:
    if mp[k] == mx:
        exit(print(k))


