from itertools import combinations, permutations, product



nums = ["0","1","2","3","4","5","6","7","8","9"]
ops = ["+", "-", "*", "/"]
structs = [
    "a x b y c z d",
    "(a x b) y c z d", "a x (b y c) z d", "a x b y (c z d)",
    "(a x b) y (c z d)",
    "(a x b y c) z d", "a x (b y c z d)",
    "((a x b) y c) z d", "(a x (b y c)) z d",
    "a x ((b y c) z d)", "a x (b y (c z d))"
]
structs = [s.replace(" ", "") for s in structs]
best = 0
ans = "0000"
for co in combinations(nums, 4):
    found = set()
    for p in permutations(co):
        a,b,c,d = p
        for s in structs:
            for o in product(ops, repeat=3):
                x,y,z = o
                new = []
                for ch in s:
                    if ch == "a": new.append(a)
                    elif ch == "b": new.append(b)
                    elif ch == "c": new.append(c)
                    elif ch == "d": new.append(d)
                    elif ch == "x": new.append(x)
                    elif ch == "y": new.append(y)
                    elif ch == "z": new.append(z)
                    else: new.append(ch)
                try:
                    num = eval("".join(new))
                except ZeroDivisionError: continue
                if not num.is_integer(): continue
                #print("".join(new))
                found.add(int(num))
    for i in range(1, 10000):
        if i not in found:
            if i > best:
                ans = "".join(co)
                best = i
            break

print(ans)
    
