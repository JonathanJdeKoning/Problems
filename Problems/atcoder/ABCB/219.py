s = input()
t = input()
u = input()
n = input()
x = [s,t,u]
new = []
for c in n:
    new.append(x[int(c)-1])
print("".join(new))
