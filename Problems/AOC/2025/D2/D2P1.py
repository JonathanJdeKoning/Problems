from itertools import *
from collections import *
ans = 0
#with open("test.in","r") as file:
with open("D2P1.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        ranges = [y for y in x.split(",") if y]
        for r in ranges:
            s, e = map(int, r.split("-"))
            for i in range(s, e+1):
                if i < 10: continue
                s = str(i)

                for d in range(1, len(s)//2+1):
                    if len(s)%d != 0: continue
                    b = list(batched(s, d))
                    if all(x==b[0] for x in b):
                        ans += i
                        break

print(ans)
        