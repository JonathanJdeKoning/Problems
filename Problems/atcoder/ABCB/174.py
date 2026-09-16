from math import dist
N, D = list(map(int, input().split()))
ans = 0
for _ in range(N):
    x, y = list(map(int, input().split()))
    
    if dist((0,0), (x,y)) <= D:
        ans += 1
print(ans)

