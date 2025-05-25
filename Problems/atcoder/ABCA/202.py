a,b,c = map(int, input().split())
t = 0
for c in [a,b,c]:
    t += 7-c
print(t)
