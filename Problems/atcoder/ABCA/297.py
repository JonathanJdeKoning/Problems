n,d = map(int, input().split())
from itertools import pairwise
for a, b in pairwise(list(map(int, input().split()))):
    if b-a <=d: print(b);exit(0)
print(-1)
