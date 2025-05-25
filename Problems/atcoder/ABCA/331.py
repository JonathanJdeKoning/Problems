months, days = map(int, input().split())

y,m,d = map(int, input().split())

d+=1
if d == days+1:
    d = 1
    m += 1
    if m ==months+1:
        m = 1
        y+= 1
print(y,m,d)
