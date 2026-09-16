from collections import defaultdict
N = int(input())

edges = defaultdict(list)

for _ in range(N):
    U, V = list(map(int, input().split()))
    edges[U].append(V)
    edges[V].append(U)

root = 1
seen = set()
dfs = [1]

while dfs:
    