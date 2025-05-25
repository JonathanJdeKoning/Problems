n,s,t = map(int, input().split())

weight = 0
ans = 0
for _ in range(n):
    d = int(input())
    weight += d
    if s<=weight<=t:
        ans += 1
print(ans)

