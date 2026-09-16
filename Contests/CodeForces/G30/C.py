def solve():
    N, M = list(map(int, input().split()))
    
    S = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    monsters = sorted(zip(B, C), key = lambda x: x[0])
    regs = []
    zers = []
    for h,c in monsters:
        if c == 0:
            zers.append(h)
        else:
            regs.append((h,c))

    bestSword = S.pop()

    regsKilled = 0
    for h, c in regs:
        if h <= bestSword:
            bestSword = max(bestSword, c)
            regsKilled += 1

    zersKilled = 0
    while zers:
        if zers[-1] > bestSword:
            zers.pop()
            continue
        else:
            zersKilled += 1
            zers.pop()
            if not S:
                break
            bestSword = S.pop()

    return regsKilled + zersKilled


    

for _ in range(int(input())):
    print(solve())