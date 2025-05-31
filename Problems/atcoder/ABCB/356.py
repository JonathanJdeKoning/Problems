n,m = map(int, input().split())
from collections import defaultdict

d = defaultdict(int)

nuts = map(int, input().split())

for i, c in enumerate(nuts):
    d[i] = c


for _ in range(n):
    dat = map(int, input().split())
    for i,c in enumerate(dat):
        d[i] -= c


if len([x for x in d.values() if x >0]) == 0:
    print("Yes")
else:
    print("No")
