from collections import deque
from itertools import pairwise
from heapq import heappop, heappush
def solve():
    N, K, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    used = set()
    teles = []
    A.sort()
    heappush(teles, (-A[0], 0))
    heappush(teles, (-(X-A[-1]), X ))
    ans = []
    for a,b in pairwise(A):
        dist = b-a
        if dist % 2 == 0:
            mid = (a+b)//2
            heappush(teles, (-(b-mid), mid))
        elif dist % 2 == 1:
            midA = (a+b)//2
            heappush(teles, (-(midA-a), midA))
            
            midB = midA+1
            heappush(teles, (-(b-midB), midB))
 
    while K:
        dist, loc = heappop(teles)
        if loc in used: continue
        posdist = -dist        
        ans.append(loc)
        used.add(loc)
        K -= 1
        if K == 0: break
        left = loc-1
        right = loc+1
 
        if left >= 0 and left not in used:
            heappush(teles, (-(posdist-1), left))
        if right <= X and right not in used:
            heappush(teles, (-(posdist-1), right))
 
        
    return " ".join(map(str, ans))
 
 
 
 
 
 
 
for _ in range(int(input())):
    print(solve())