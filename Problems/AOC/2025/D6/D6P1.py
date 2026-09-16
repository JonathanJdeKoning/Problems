from itertools import *
from collections import *
from functools import reduce
ans = 0
M = []
A = []
with open("test.in","r") as file:
#with open("data.in","r") as file:
    for line in file.readlines():
        
        x = line.replace("  ", " ").split()
        M.append(x)
        
for row in M: print(row)
for j in range(len(M[0])):
    nums = [row[j] for row in M[:-1]]
    
    op = M[-1][j]

    ans += eval(op.join(nums))


print(ans)
        