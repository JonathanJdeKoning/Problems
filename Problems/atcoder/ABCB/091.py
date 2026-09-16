from collections import defaultdict
N = int(input())
n = defaultdict(int)
for _ in range(N):
    n[input()] += 1

M = int(input())
m = defaultdict(int)
for _ in range(M):
    m[input()] += 1

best = 0
for k in n:
    best = max(best, n[k] - m[k])
print(best)



