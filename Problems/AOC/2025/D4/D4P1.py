from itertools import *
from collections import *
ans = 0
directions = [(x,y) for x in [-1, 0, 1] for y in [-1,0,1] if (x,y) != (0,0)]
M = []
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        M.append(list(x))

R = len(M)
C = len(M[0])

for i in range(R):
    for j in range(C):
        if M[i][j] != "@": continue

        adj = 0
        for dy, dx in directions:
            ny, nx = dy+i, dx+j

            if ny not in range(R) or nx not in range(C): continue
            if M[ny][nx] != "@": continue
            adj += 1
        if adj < 4:
            ans += 1




print(ans)
        