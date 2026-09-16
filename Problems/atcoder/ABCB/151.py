N ,K, M = list(map(int, input().split()))

A = list(map(int, input().split()))

tot = sum(A)

for i in range(K+1):
    if (tot + i) / N >= M:
        exit(print(i))
print(-1)