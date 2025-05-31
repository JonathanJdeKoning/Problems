from itertools import accumulate
N, M = map(int, input().split())
turrets = []

suff = [0]*(N+1)
for _ in range(M):
    l, r = list(map(int, input().replace(","," ").split()))
    l -= 1
    r -= 1
    suff[l] += 1
    suff[r+1] -= 1


prefix = list(accumulate(suff))
print(min(prefix[:-1]))
