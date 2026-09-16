from math import dist
N = int(input())

points = []

for _ in range(N):
    x,y = list(map(int, input().split()))
    points.append((x,y))

best = 0
for i in range(len(points)-1):
    for j in range(len(points)):
        best = max(best, dist(points[i], points[j]))
print(best)
