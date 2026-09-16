N = int(input())

ans = 0 

points = []
for _ in range(N):
    x,y = list(map(int, input().split()))
    points.append((x,y))

for i in range(N-1):
    x, y = points[i]
    for j in range(i+1, N):
        a,b = points[j]
        if a - x == 0: continue
        slope = (b-y)/(a-x)

        if slope >= -1 and slope <= 1:
            ans += 1
print(ans)

