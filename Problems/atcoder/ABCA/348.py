n = int(input())
out = []
for i in range(1, n+1):
    if i%3==0: out.append("x")
    else: out.append("o")
print("".join(out))
