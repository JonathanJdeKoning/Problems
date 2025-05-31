n = int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))

for i, (x1,y1) in enumerate(points):
    mxdist = 0
    ans = 0
    for j, (x2, y2) in enumerate(points):
        dist = ((x1-x2)**2+(y1-y2)**2)**0.5
        if dist > mxdist:
            mxdist = dist
            ans = j+1
    print(ans)



