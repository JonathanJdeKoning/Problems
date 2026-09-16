from itertools import *
from collections import *
from heapq import *
from functools import *
ans = 0
N = 0
MX = 0
need = [] 
buttons = []
jolt = []


def solve():
    seen = set()
    q = deque([0])
    steps = -1
    while q:

        steps += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == need: return steps
            if curr in seen: continue
            seen.add(curr)
            for b in buttons:
                new = curr^b
                if new <=MX and new not in seen: q.append(new)

    
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip().split()
        N = len(l[0])-2
        MX = 2**(N)-1
        need = int(l[0][1:-1][::-1].replace(".","0").replace("#","1"), 2)
        jolt = list(map(int, l[-1][1:-1].split(",")))
        buttonString = l[1:-1]
        buttons = [list(map(int, b[1:-1].split(","))) for b in buttonString]
        for i, b in enumerate(buttons):
            n = 0
            for tog in b:
                n += 1<<tog
            buttons[i] = n
        print(buttons)
        ans += solve()
        
print(ans)