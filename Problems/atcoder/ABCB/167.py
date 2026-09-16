A, B, C, K = list(map(int, input().split()))

ans = 0

ones =min(K, A)
ans += ones
K -= ones
if not K: exit(print(ans))

zs = min(K, B)
K -= zs
if not K: exit(print(ans))

print(ans - K)