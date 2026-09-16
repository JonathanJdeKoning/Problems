from collections import defaultdict
from functools import cache
def tri(n): return (n*(n+1))//2
def square(n): return (n*n)
def pent(n): return (n*(3*n-1))//2
def hex(n): return n*(2*n-1)
def hept(n): return n*((5*n-3))//2
def oct(n): return n*(3*n-2)


mp = defaultdict(list)

n=1
while True:
    a = tri(n)
    b = square(n)
    c = pent(n)
    d = hex(n)
    e = hept(n)
    f = oct(n)

    if a >= 10000: break

    if a in range(1000, 10000): mp[3].append(a)
    if b in range(1000, 10000): mp[4].append(b)
    if c in range(1000, 10000): mp[5].append(c)
    if d in range(1000, 10000): mp[6].append(d)
    if e in range(1000, 10000): mp[7].append(e)
    if f in range(1000, 10000): mp[8].append(f)

    n += 1

edges = defaultdict(list)

for numType, nums in mp.items():
    for num in nums:
        end = num%100
        for k,v in mp.items():
            for n2 in v:
                start = (n2-(n2%100))//100
                if start == end:
                    edges[(num, numType)].append((n2,k))

usedTypes = set()
usedNums = set()

def findCycle(num, numType, startNum):
    usedTypes.add(numType)
    usedNums.add(num)

    for newNum, newType in edges[(num, numType)]:
        if len(usedTypes) == 6 and newNum == startNum: exit(print(sum(usedNums)))

        if newType in usedTypes: continue
        if newNum in usedNums: continue

        findCycle(newNum, newType, startNum)

    usedTypes.discard(numType)
    usedNums.discard(num)

for n, t in list(edges.keys()):
    findCycle(n, t, n)