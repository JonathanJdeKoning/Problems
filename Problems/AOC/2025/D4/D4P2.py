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
ADJ = [[-1]*C for _ in range(R)]
q = deque([])
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
            q.append((i,j))

        ADJ[i][j] = adj

print("h")
seen = set()
while q:
    cy, cx = q.popleft()
    if (cy, cx) in seen: continue
    seen.add((cy, cx))
    ans += 1
    M[i][j] = "."
    for dy, dx in directions:
        ny, nx = dy+cy, dx+cx
        if (ny, nx) in seen: continue
        if ny not in range(R) or nx not in range(C): continue
        if M[ny][nx] != "@": continue
        ADJ[ny][nx] -= 1
        if ADJ[ny][nx] < 4:
            q.append((ny, nx))
print(ans)
        