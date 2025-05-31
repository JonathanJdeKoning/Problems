from collections import defaultdict, deque
from heapq import heappush, heappop
N, M = list(map(int, input().replace(","," ").split()))

edges = defaultdict(list)
for _ in range(M):
    u,v,w = list(map(int, input().replace(","," ").split()))
    u -= 1
    v -= 1
    edges[u].append((w, v))

h = [(0,0)]
seen = set()

while h:
    currVal, currNode = heappop(h)
    if (currVal, currNode) in seen: continue
    seen.add((currVal, currNode))

    if currNode == N-1:
        exit(print(currVal))

    for edgeVal, edgeNode in edges[currNode]:

        newVal = currVal | edgeVal
        if (newVal, edgeNode) in seen: continue
        heappush(h, (newVal, edgeNode))

