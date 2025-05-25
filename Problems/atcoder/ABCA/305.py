n = int(input())
p = []
for i in range(n,n+6):
    if i%5==0: p.append(i); break
for i in range(n, n-6,-1):
    if i%5 == 0:p.append(i); break

p = sorted(p, key=lambda x: abs(x-n))
print(p[0])
