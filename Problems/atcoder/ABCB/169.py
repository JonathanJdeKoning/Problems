N = int(input())
A = list(map(int, input().split()))
if 0 in A: exit(print(0))
prod = 1
for num in A:
    prod *= num
    if prod > int(1e18): exit(print(-1))
print(prod)