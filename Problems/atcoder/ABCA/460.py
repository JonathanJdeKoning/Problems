N, M = map(int, input().split())

ans = 0
while M != 0:
    ans += 1
    M = N%M

print(ans)
