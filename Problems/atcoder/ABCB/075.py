H, W = map(int, input().split())

mat = [list(input()) for _ in range(H)]

new = [[None]*W for _ in range(H)]

directions = [(x,y) for x in (-1,0,1) for y in (-1,0,1) if (x,y) != (0,0)]

for i in range(H):
    for j in range(W):
        count = 0
        cell = mat[i][j]
        if cell == "#": new[i][j] = cell; continue
    
        for dy, dx in directions:
            ny, nx = i+dy, dx + j
            if min(ny, nx)== -1 or ny == H or nx == W:
                continue
            if mat[ny][nx] == "#":
                count += 1
        new[i][j] = str(count)

for row in new:
    print("".join(row)) 