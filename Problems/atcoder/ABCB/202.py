S = input()
new = []

for c in S[::-1]:
    if c == "6": new.append("9")
    elif c == "9": new.append("6")
    else: new.append(c)

print("".join(new))