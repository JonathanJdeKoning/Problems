from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0
M = []
A = []
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip()
        x, y= map(int, l.split(","))

        A.append((x,y))

for i in range(len(A)-1):
    ax, ay = A[i]
    for j in range(i+1, len(A)):
        bx, by = A[j]
        area = (1+abs(ax-bx)) * (1+abs(ay-by))
        ans = max(ans, area)
        
print(ans)