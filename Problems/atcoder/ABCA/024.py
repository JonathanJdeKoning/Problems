a,b,c,k = map(int, input().split())
s,t = map(int, input().split())

peeps =s+t
total = s*a + b*t

if peeps >= k:
    total -= (c*peeps)

print(total)
