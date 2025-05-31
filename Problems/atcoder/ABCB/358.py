n,a = map(int, input().split())
t = list(map(int, input().split()))

tot = 0
for p in t:
    tot = max(tot, p)
    tot += a

    print(tot)
