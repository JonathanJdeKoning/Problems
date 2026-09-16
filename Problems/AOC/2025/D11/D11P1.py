from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0
A = []
edges = {}
parents = defaultdict(list)
roots = set()
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip().split()
        u = l[0][:-1]
        edges[u] = l[1:]
        for v in edges[u]:
            parents[v].append(u)
        roots.add(u)
for k,v in edges.items():
    for node in v:
        roots.discard(node)
root = roots.pop()
@cache
def numWays(node):
    if node == "you": return 1
    return sum([numWays(p) for p in parents[node]])
print(numWays("out"))