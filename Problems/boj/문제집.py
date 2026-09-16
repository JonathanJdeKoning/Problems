from collections import defaultdict
from graphlib import TopologicalSorter
from heapq import heappush, heappop
N, K = list(map(int, input().split()))

children = {}
parents = {}

for i in range(1, N+1):
    children[i] = []
    parents[i] = 0 
h = []

for _ in range(K):
    U, V = list(map(int, input().split()))
    children[U].append(V)
    parents[V] += 1

for k in parents:
    if parents[k] == 0:
        heappush(h, k)

ans = []

while h:
    x = heappop(h)
    ans.append(x)
    for child in children[x]:
        parents[child] -= 1
        if parents[child] == 0:
            heappush(h, child)
            del parents[child]
    del children[x]
print(" ".join(map(str, ans)))
