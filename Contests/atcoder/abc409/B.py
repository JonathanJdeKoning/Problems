from collections import defaultdict, Counter
from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))

fq = Counter(A)


def cond(x):
    cnt = 0
    for k in fq:
        if k >= x:
            cnt += fq[k]
    return cnt >= x

print(bisect_right(range(int(1e9+1)), False, key=lambda x: not cond(x))-1)
