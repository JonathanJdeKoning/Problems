from collections import defaultdict
N ,M = list(map(int, input().split()))
liked = defaultdict(int)
for _ in range(N):
    data = list(map(int, input().split()))
    for c in data[1:]:
        liked[c] += 1

print(list(liked.values()).count(N))
