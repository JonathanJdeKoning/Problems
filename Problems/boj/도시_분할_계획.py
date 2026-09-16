from collections import defaultdict
from heapq import heappush, heappop
N, K = list(map(int, input().split()))


h = []
edges = defaultdict(list)
seen = set()
for _ in range(K):
    U, V, W = list(map(int, input().split()))
    edges[U].append((V, W))
    edges[V].append((U, W))

for edgeNode, edgeWeight in edges[1]:
    heappush(h, (edgeWeight, edgeNode))

sumWeights = []
seen.add(1)
while h:
    edgeWeight, edgeNode = heappop(h)
    if edgeNode in seen: continue
    seen.add(edgeNode)

    sumWeights.append(edgeWeight)

    for newNode, newWeight in edges[edgeNode]:
        if newNode in seen: continue
        heappush(h, (newWeight, newNode) )
print(sum(sumWeights) - max(sumWeights))





    

