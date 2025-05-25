n, s, t = input().split()

x =input()
new = []
for c in x:
    if c != s:
        new.append(t)
    else:
        new.append(c)
print("".join(new))