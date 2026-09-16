from collections import deque
from heapq import *
from itertools import pairwise
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    mp = {}
    h = []
    for i in range(len(A)):
        mp[i] = A[i]
        heappush(h, (max(A[i], A[(i+1)%N]), i, A[i], A[(i+1)%N]))
    
    while len(h) != 1:
        mx, start, a, b = heappop(h)
        if mp[start] != a or mp[(start+1)%N] != b:
            heappush(h, (max(mp[start], mp[(start+1)%N]), start, mp[start], mp[(start+1)%N]))
        else:
            ans += mx
            mp[start] = mx
            mp[(start+1)%N] = mx
    print(ans)
    
            



    
for _ in range(int(input())):
    solve()