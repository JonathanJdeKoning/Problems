R, C, n = map(int, input().split())
mat = [list("."*C) for _ in range(R)]

y,x = 0, 0 
def new_pos(y,x):
    if y ==R:
        y = 0
    if y ==-1:
        y = R-1
    if x ==C:
        x = 0
    if x ==-1:
        x = C-1
    return y,x
dir = 0
directions = [(-1,0), (0,1), (1,0), (0,-1)]

for _ in range(n):
    cell = mat[y][x]
    
    if cell == ".":
        mat[y][x] = "#"
        dir = (dir+1)%4
    elif cell == "#":
        mat[y][x] = "."
        dir  = (dir-1)%4
    dy,dx = directions[dir]
    y,x = new_pos(y+dy, x+dx)

for row in mat:
    print("".join(row))


