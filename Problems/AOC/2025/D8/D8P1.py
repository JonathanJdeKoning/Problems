from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

M = []
A = []
h = []
from math import dist
dsu = DisjointSetUnion(1001)
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip()
        x,y,z = map(int, l.split(","))
        A.append((x,y,z))

for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        heappush(h,(dist(A[i], A[j]), i, j))

while h:
    d, i, j = heappop(h)
    if dsu.find(i) == dsu.find(j): continue
    dsu.union(i,j)
    print(A[i][0]*A[j][0])
        