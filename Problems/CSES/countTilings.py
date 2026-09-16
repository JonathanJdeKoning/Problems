from functools import cache
from itertools import groupby

N, M = list(map(int, input().split()))
MOD = int(1e9)+7

def rep(mask):
    r = {True:"#", False:"."}
    print("\n".join([r[x] for x in getCol(mask)]))
    print()

def bigRep(mask):
    rep(mask)
    for p in colFills(mask):
        rep(p)

@cache 
def getCol(mask):
    global N, M
    return [bool(mask & (1<<i)) for i in range(N)]

@cache
def colFills(mask, startI):
    global N, M
    col = getCol(mask)
    newmask = 0
    poss = [0]
    i = startI
    while i < N:
        if col[i]:
            i += 1
            continue

        if i == N-1 or col[i+1]:
            poss = [p + 2**i for p in poss]
            i += 1
            continue

        # Not col[i] and not col[i+1]
        
        poss.extend([p + 2**i + 2**(i+1) for p in poss])
        i += 2
    return poss

    

@cache
def countTilings(j, mask):
    global N, M
    if j == M: return 0
    if j == M-1:
        col = getCol(mask)
        if all(col): return 1
        for k, v in groupby(col):
            v = list(v)
            if not k and len(v)%2 == 1: return 0
        return 1
    ans = 0
    for p in colFills(mask):
        ans += countTilings(j+1, p)
    return ans%MOD

    


print(countTilings(0, 0))