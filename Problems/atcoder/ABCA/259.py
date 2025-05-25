n,m,x,t,d = map(int, input().split())
z = {}
for i in range(x, n+1):
    z[i] = t
for i in range(x-1,-1,-1):
    t -= d
    z[i] = t
print(z[m])
