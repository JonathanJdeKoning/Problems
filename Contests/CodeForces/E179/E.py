for _ in range(int(input())):
    N, Q = list(map(int, input().split()))
    S = input()

    b2a = 0
    b2c = 0
    c2a = 0
    c2b = 0

    for _ in range(Q):
        f, t = input().split()
        if f == t or f == "a": continue
        elif f == "b":
            if t == "a": b2a += 1
            else: b2c += 1
        elif f == "c":
            if t == "a": c2a += 1
            else: c2b += 1
    
    new = []
    for i, c in enumerate(S):
        if c == "a": continue
        if c == "b":
            if b2a:
                b2a -= 1
                new.append("a")
            elif b2c and c2a:
                b2c -= 1
                c2a -= 1
                new.append("a")
            else:
                new.append(c)
        if c == "c":
            if c2a:
                c2a -= 1
                new.append("a")
            elif c2b and b2a:
                c2b -= 1
                b2a -= 1
                new.append("a")
            elif c2b:
                c2b -= 1
                new.append("b")
            else:
                new.append(c)
    print("".join(new))

        
