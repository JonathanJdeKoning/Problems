from itertools import *
from collections import *
curr = 50
ans = 0
with open("D1P1.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        if x[0] == "L":
            curr = (curr - int(x[1:]))%100
        else:
            curr = (curr + int(x[1:]))%100

        if curr == 0:
            ans += 1
print(ans)

        