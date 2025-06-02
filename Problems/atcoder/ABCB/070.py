a,b,c,d = map(int, input().split())
s = set()
for i in range(a, b):
    s.add(i)
ans = 0
for i in range(c, d):
    if i in s:
        ans += 1
print(ans)