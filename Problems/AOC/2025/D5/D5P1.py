from itertools import *
from collections import *
ans = 0
ranges = True
R = []
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        if not x:
            ranges = False
            continue

        if ranges:
            R.append(tuple(map(int, x.split("-"))))
        else:
            y = int(x)
            for s, e in R:
                if y >= s and y <= e:
                    ans += 1
                    break



print(ans)
        