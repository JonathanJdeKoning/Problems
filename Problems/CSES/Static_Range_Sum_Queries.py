from itertools import accumulate
N, Q = list(map(int, input().split()))

A = list(map(int, input().split()))
pref = list(accumulate(A, initial=0))

for _ in range(Q):
    l, r = list(map(int, input().split()))
    l-=1
    r -=1
    print(pref[r+1] - pref[l])