from math import dist
N, D = list(map(int, input().split()))
points = [tuple(list(map(int, input().split()))) for _ in range(N)]

ans = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        if dist(points[i], points[j]).is_integer(): ans += 1
print(ans) 