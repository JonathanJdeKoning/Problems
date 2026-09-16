N = int(input())
P = list(map(int, input().split()))
ans = 0
X = P[N-2]
while X != 1:
    ans += 1
    X = P[X-2]

print(ans+1)
