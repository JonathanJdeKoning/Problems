N , X = list(map(int, input().split()))

A = []
best = 1000000000
for _ in range(N):
    x, t = list(map(int, input().split()))
    if t <= X:
        best = min(best, x)
if best == 1000000000:
    print("TLE")
else:
    print(best)