N ,K = list(map(int, input().split()))

bad = set(list(range(1, N+1)))

for _ in range(K):
    n = int(input())
    d = list(map(int, input().split()))
    for num in d:
        bad.discard(num)
print(len(bad))
