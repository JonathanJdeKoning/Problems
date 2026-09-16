from copy import deepcopy
R, C = list(map(int, input().split()))
y, x, d = list(map(int, input().split()))

dy, dx = {0:(-1,0), 1: (0,1), 2:(1,0), 3:(0,-1)}[d]
M = [list(map(int, input().split())) for _ in range(R)]
clean = deepcopy(M)

dirs = [(-1,0),(0,-1),(1,0),(0,1)]
mp = {
    (-1,0):(0,-1),
    (0,-1):(1,0),
    (1,0):(0,1),
    (0,1):(-1,0),

}
ans = 0
while True:
    if clean[y][x] == 0:
        clean[y][x] = 1
        ans += 1
    for ty, tx in dirs:
        ny, nx = ty+y, tx+x
        if M[ny][nx] == 1: continue
        if clean[ny][nx] == 0:
            break
    else: 
        if M[y-dy][x-dx] == 1: break
        y -= dy
        x -= dx
        continue
    dy, dx = mp[(dy, dx)]
    if M[y+dy][x+dx] == 0 and clean[y+dy][x+dx] == 0:
        y += dy
        x += dx



print(ans)


