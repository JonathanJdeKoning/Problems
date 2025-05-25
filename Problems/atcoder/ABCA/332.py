n,s,k = map(int, input().split())
t = 0
for _ in range(n):
    p,q = map(int, input().split())
    t+= p*q
if t < s: t += k
print(t)
