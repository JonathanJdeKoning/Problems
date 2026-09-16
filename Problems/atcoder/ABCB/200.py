N, K = list(map(int, input().split()))

for _ in range(K):
    if N %200 == 0:
        N //=200
        continue

    N = int(str(N) + "200")

print(N)