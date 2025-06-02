N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for _ in range(K):
    ans += A.pop()
print(ans)