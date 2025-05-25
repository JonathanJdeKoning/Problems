input()
p = list(map(int, input().split()))
p1 = p[0]
mx = max(p)
if p1 == mx:
    if p.count(mx) >=2: print(1)
    else: print(0)
else:
    print(1+(mx-p1))
