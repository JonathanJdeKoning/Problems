N = int(input())

points = []
for _ in range(N):
    X, Y = list(map(int, input().split()))
    points.append((X, Y))
points.append(points[0])
total = 0
for i in range(len(points)-1):
    total += points[i][0]*points[i+1][1]
    total -= points[i][1]*points[i+1][0]
print(round(abs(total/2), 1))
    