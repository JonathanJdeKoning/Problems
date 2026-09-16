from math import dist, inf

N, K = list(map(int, input().split()))

A = set(list(map(int, input().split())))

peeps = []
lights = []
for i in range(1, N+1):
    x, y = list(map(int, input().split()))
    if i in A:
        lights.append((x,y))
    else:
        peeps.append((x,y))
ans = 0
for p in peeps:
    mn = inf
    for l in lights:
        d = dist(p, l)
        mn = min(d, mn)
    ans = max(ans, mn)
print(ans)