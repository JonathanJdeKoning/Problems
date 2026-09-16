from itertools import *
from collections import *
ans = 0
#with open("test.in","r") as file:
with open("D3P1.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        y = 0
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                y = max(y, int(x[i]+x[j]))
        ans += y
        print(y)


print(ans)
        