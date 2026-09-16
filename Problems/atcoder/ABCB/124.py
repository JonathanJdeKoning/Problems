N = int(input())
A = list(map(int, input().split()))

mx= 0
ans = 0
for num in A:
    if num >= mx:
        mx = num
        ans += 1
print(ans)