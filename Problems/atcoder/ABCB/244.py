N = int(input())
T = input()
x,y = 0,0

dy, dx = (0, 1)
mp = {
    (0,1):(-1,0),
    (0,-1):(1,0),
    (-1,0):(0,-1),
    (1,0):(0,1)
}
for c in T:
    if c == "R":
        dy, dx = mp[(dy, dx)]       
    elif c == "S":
        y += dy
        x += dx
print(x, y)