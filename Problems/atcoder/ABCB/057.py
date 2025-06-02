N , M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
checks = [list(map(int, input().split())) for _ in range(M)]

for sx, sy in students:
    dists = [abs(sy - cy) + abs(sx - cx) for cx, cy in checks]
    best = min(dists)
    print (dists.index(best) + 1)