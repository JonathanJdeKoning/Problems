from math import gcd
from collections import Counter
m = 2
n = 1
L = 1500000
def nextPrim():
    global n
    global m
    if n<m-2: n += 2
    else:
        m += 1
        if m%2==0:
            n = 1
        else:
            n = 2

fq = Counter()
done = False
seen = set()
while True:
    if done: break
    k = 1
    while True:
        a = k * (m**2 - n**2)
        b = k * (2*m*n)
        c = k * (m**2+n**2)
        l = a+b+c
        if (a,b,c) in seen: break
        if l > L*2 and k==1:
            done=True
            break
        if l > L: break
        fq[l] += 1
        seen.add((a,b,c))
        k += 1
    nextPrim()


ans = 0
for k,v in fq.items():
    if v == 1:
        ans += 1
print(ans)
