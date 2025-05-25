n = input()
o = []
for c in n:
    if c=="1": o.append("9")
    elif c=="9": o.append("1")
    else:
        o.append(c)

print("".join(o))
