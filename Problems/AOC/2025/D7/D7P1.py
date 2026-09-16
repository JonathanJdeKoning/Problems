from itertools import *
from collections import *
from functools import reduce
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

dfs = [(sy+1, sx)]
seen = set()
R, C = len(M), len(M[0])
while dfs:
    cy, cx = dfs.pop()
    if (cy, cx) in seen: continue
    below = (cy+1, cx)
    if below[0] == R: continue
    if below in seen: continue
    print(below)
    if M[below[0]][below[1]] == "^":
        ans += 1
        dfs.append((below[0], below[1]+1))
        dfs.append((below[0], below[1]-1))
        seen.add(below)
    else:
        dfs.append((below[0], below[1]))

print(ans)


    





print(ans)
        