N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = sum(1 for x in A if K <= x)

print(ans)
