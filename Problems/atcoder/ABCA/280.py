n,m  = map(int, input().split())
t = 0
for _ in range(n): t += input().count("#")
print(t)
