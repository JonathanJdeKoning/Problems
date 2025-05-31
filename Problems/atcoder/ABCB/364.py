H, W = list(map(int, input().split()))
y, x = list(map(int, input().split()))
y -= 1 
x -= 1
mat = [list(input()) for _ in range(H)]
instructions = input()

directions = {
    "U": (-1,0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0,-1)
}

for instruction in instructions:
    dy, dx = directions[instruction]

    newY, newX = y+dy, x+dx

    if min(newY,newX) == -1 or newY==H or newX==W: continue
    if mat[newY][newX] == "#": continue

    y, x = newY, newX

print(y+1, x+1)
