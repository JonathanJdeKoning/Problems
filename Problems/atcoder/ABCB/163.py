N, M = list(map(int, input().split()))

print(max(-1, N - sum(list(map(int, input().split())))))
