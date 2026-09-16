from collections import defaultdict
N, L = list(map(int, input().split()))
if L % 3 != 0: exit(print(0))

A =list(map(int, input().split()))

pos = {}
loc = defaultdict(list)

for i, num in enumerate(A):
    pos[num] = i


currPoint = 1
currPos = 0
loc[currPos].append(currPoint)

while True:
    if currPoint == N: break
    currPos = (currPos + A[currPoint-1]) % (L)
    currPoint += 1

    
    loc[currPos].append(currPoint)



seen = set()
jump = L // 3
ans = 0
for l in loc:
    if l in seen: continue
    m = (l + jump) % L
    n = (m + jump) % L

    if m not in loc or n not in loc: continue

    seen.add(l)
    seen.add(m)
    seen.add(n)

    ans += len(loc[l]) * len(loc[m]) * len(loc[n])

print(ans)


