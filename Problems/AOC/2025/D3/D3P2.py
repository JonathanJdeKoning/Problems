from itertools import *
from collections import *
ans = 0
#with open("test.in","r") as file:
with open("D3P1.in","r") as file:
    for line in file.readlines():
        x = list(map(int, line.strip()))
        y = []
        up = 0
        while len(y) != 12:
            mx = max(x[up:(len(x)-11)+len(y)])
            y.append(mx)
            up = (x[up:].index(mx)+1) + up
        print(y)
        ans+=int("".join([str(x) for x in y])) 


print(ans)
        