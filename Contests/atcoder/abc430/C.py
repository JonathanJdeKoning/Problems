from collections import defaultdict
from bisect import bisect_left
N, A, B = list(map(int, input().split()))
S = input()
ans = 0
mp = defaultdict(list)
for i, c in enumerate(S):
    mp[c].append(i)

for i, c in enumerate(S):
    closestB = bisect_left(mp["b"], i)
    upto = closestB + (B-1) 
    if upto >= len(mp["b"]):
        uptoIDX = len(S)
    else:
        uptoIDX = mp["b"][upto]

    closestA = bisect_left(mp["a"], i)
    startingFrom = closestA + (A-1)

    if startingFrom >= len(mp["a"]):
        continue
    else:
        startingFromIDX = mp["a"][startingFrom]
        

    if startingFromIDX <= uptoIDX:
        #print(i, c, startingFromIDX, uptoIDX)
        ans += uptoIDX - startingFromIDX
print(ans)
