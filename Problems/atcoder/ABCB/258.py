N = int(input())
M = []
for _ in range(N):
    R = [int(x) for x in input()]
    M.append(R)

mx = 0
dirs = [(x,y) for x in [0,1,-1] for y in [0,1,-1] if (x,y) != (0,0)]

for dy, dx in dirs:
    for i in range(N):
        for j in range(N):
            num = []
            for k in range(N):
                num.append(M[(i+k*dy)%N][(j+k*dx)%N])
            mx = max(mx, int("".join([str(x) for x in num])))

print(mx)
            
