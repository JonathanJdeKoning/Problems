n = int(input())
d = {}
p = list(map(int, input().split()))

for i, c in enumerate(p):
    d[c] = i

q = int(input())

for _ in range(q):
    a,b = map(int, input().split())

    x,y = d[a], d[b]

    if x <y:
        print(a)
    else:
        print(b)
