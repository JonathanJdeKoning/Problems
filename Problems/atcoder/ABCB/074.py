N = int(input())
K = int(input())

A = list(map(int, input().split()))

ans = 0
for num in A:
    ans += min(abs(num), abs(num - K)) * 2

print(ans)
