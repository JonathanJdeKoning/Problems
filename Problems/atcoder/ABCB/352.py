s = input()
t = input()


curr= 0
out = []
for i,c in enumerate(t):
    if c ==s[curr]:
        out.append(i+1)
        curr += 1
print(" ".join(map(str, out)))
