from itertools import *
from collections import *
from functools import reduce
ans = 0
M = []
A = []
with open("data.in","r") as file:
    for line in file.readlines():
        M.append(list(line.replace("\n", "")))
M = list(zip(*M))[::-1]

stack = []
for row in M:
    if len(set(row)) == 1: continue
    num = int("".join([x for x in row[:-1] if x != " "]))
    stack.append(num)
    if row[-1] != " ":
        ans += eval(row[-1].join(list(map(str, stack))))
        stack = []
print(ans)
        