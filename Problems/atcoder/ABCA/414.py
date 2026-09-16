N, L, R = map(int, input().split())

ans = 0
for _ in range(N):
    l, r = map(int, input().split())
    if l <= L and r >= R:
        ans += 1
print(ans)
    
