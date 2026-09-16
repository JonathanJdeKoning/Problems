H, W, Y, X = list(map(int, input().split()))
X -= 1
Y -= 1
mat = [list(input()) for _ in range( H )]

directions = [(-1,0),(0,1),(1,0),(0,-1)]
ans = 1
for dy, dx in directions:
    cy, cx = Y, X
    while True:
        cy += dy
        cx += dx
        if min(cy, cx) == -1 or cy == H or cx == W: break
        if mat[cy][cx] == "#" : break
        ans += 1

print(ans) 
