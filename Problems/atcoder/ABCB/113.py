N = int(input())
T, A = list(map(int, input().split()))

H = list(map(int, input().split()))

ans = 1
best = 1000000000
for i, num in enumerate(H):
    el = T - num * 0.006
    if abs(el - A) < best:
        best = abs(el - A)
        ans = i + 1
print(ans)
