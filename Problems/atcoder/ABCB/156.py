N , K = list(map(int, input().split()))


ans = 0

while N:
    m = N % K
    N -= m
    N //= K
    ans += 1
print(ans)