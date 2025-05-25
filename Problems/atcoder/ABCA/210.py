n,a,x,y = map(int, input().split())
cabbages = 0
total = 0
while True:
    cabbages += 1
    if cabbages > a:
        total += y
    else: total += x
    if cabbages == n: break
print(total)
