from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(20000)

N, E = list(map(int, input().split()))
edges = {}
revEdges = {}
for i in range(1, N+1):
    edges[i] = []
    revEdges[i] = []
for _ in range(E):
    U, V = list(map(int, input().split()))
    edges[U].append(V)
    revEdges[V].append(U)



seen = set()
revOrder = []
def dfs(node):
    if node in seen: return
    seen.add(node)
    for edge in edges[node]:
        if edge in seen: continue
        dfs(edge)
    revOrder.append(node)

for node in edges:
    if node in seen: continue
    dfs(node)
revOrder = revOrder[::-1]

seen = set()
scc = []
def dfs(node):
    if node in seen: return
    seen.add(node)
    for edge in revEdges[node]:
        if edge in seen: continue
        dfs(edge)
    scc[-1].append(node)

for node in revOrder:
    if node in seen: continue
    scc.append([])
    dfs(node)

print(len(scc))
for group in sorted(scc, key=min):
    print(" ".join(map(str, sorted(group))),-1)
