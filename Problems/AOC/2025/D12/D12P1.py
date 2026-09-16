from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0
A = []
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip().split()
        if not l: continue
        if "x" not in l[0]: continue
        H, W = map(int, l[0][:-1].split("x"))
        totalBlocks = sum(list(map(int, l[1:])))
        defFit = (H//3) * (W//3)
        if defFit >= totalBlocks:
            ans += 1
        else:

            print(defFit,totalBlocks)

print(ans)