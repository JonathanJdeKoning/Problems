from itertools import *
from collections import *
from functools import reduce, cache
ans = 0
M = []
A = []
sy, sx = (0,0)
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i ,line in enumerate(file.readlines()):
        M.append(list(line.strip()))
        if "S" in line.strip():
            sy = i
            sx = line.strip().index("S")
R, C = len(M), len(M[0])
@cache
def dp(cy, cx):
    if cy == R: return 1
    if M[cy][cx] == "^":
        return dp(cy, cx+1) + dp(cy, cx-1)
    else: return dp(cy+1, cx)


print(dp(sy+1, sx))
        