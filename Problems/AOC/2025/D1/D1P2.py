from itertools import *
from collections import *
curr = 50
ans = 0
with open("D1P1.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        n = int(x[1:])
        if x[0] == "L":
            while n:
                curr = (curr-1)%100
                n -= 1
                if curr == 0: ans += 1
        else:
            while n:
                curr = (curr+1)%100
                n -= 1
                if curr == 0: ans += 1


print(ans)

        