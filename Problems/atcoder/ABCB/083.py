N, A, B = list(map(int, input().replace(","," ").split()))
ans = 0
for i in range(1, N+1):
    digsum = sum(int(x) for x in str(i))
    if digsum in range(A, B+1):
        ans += i
print(ans)