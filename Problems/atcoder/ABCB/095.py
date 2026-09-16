N, X = list(map(int, input().split()))
best = int(1e9)
ans = N
for _ in range(N):
    D = int(input())
    X -= D
    best = min(best, D)
ans += X // best
print(ans)