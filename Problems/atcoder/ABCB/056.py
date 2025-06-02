w, a,b = map(int, input().split())
a,b = min(a,b), max(a,b )
dist = b - (a+w)
if dist <= 0:
    print(0)
else:
    print(dist)