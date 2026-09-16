from random import randint
from math import lcm
from functools import reduce


A = set([2])

for r in range(3, int(1e9)):
    if r in A: continue
    for x in A:
        if (r % x) % 2 == 0:
            break
    else:
        A.add(r)
        print(A)


