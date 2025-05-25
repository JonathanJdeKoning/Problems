out = []
t = 1
for _ in range(1+2*(int(input()))):
    out.append(t)
    t^=1
print("".join(map(str, out)))
