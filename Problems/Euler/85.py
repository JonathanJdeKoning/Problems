from math import comb
from functools import cache
@cache
def numRects(C, R):
    ans = 0
    seen = set()
    for c in range(C, 0,-1):
        for r in range(R, 0, -1):
            if (c, r) in seen: continue
            ans += smallsInBig(c, r, C, R)
            seen.add((c,r))

    return ans 


def smallsInBig(c, r, C, R):
    ans =  (C-(c-1)) * (R-(r-1))

    #print(f"{c=}, {r=}, {ans=}")
    return ans


R = 1
C = 1
target = 2000000
best = 0
while True:
    a = numRects(C, R)
    if abs(a-target) < abs(best-target):
        best = a
        print(best,C*R)
    if a > target:
        R += 1
        C = 1
        continue
    C += 1