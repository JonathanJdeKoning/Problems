N, K = list(map(int, input().split()))
ans = []
for i in range(K - (N-1), K+ N):
    ans.append(i)
print(*ans)