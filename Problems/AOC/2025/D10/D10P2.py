from itertools import *
from collections import *
from heapq import *
from functools import *
from z3 import Ints, Optimize, sat
ans = 0
N = 0
MX = 0
need = [] 
buttons = []
jolt = []
    
#with open("test.in","r") as file:
with open("data.in","r") as file:
    for i, line in enumerate(file.readlines()):
        l = line.strip().split()
        N = len(l[0])-2
        jolt = list(map(int, l[-1][1:-1].split(",")))
        buttonString = l[1:-1]
        buttons = [list(map(int, b[1:-1].split(","))) for b in buttonString]
        o = Optimize()
        vars = Ints(f"n{i}" for i in range(len(buttons)))
        for var in vars: o.add(var >= 0)

        for i, j in enumerate(jolt):
            eq = 0
            for b, button in enumerate(buttons):
                if i in button:
                    eq += vars[b]
            o.add(eq == j)
        o.minimize(sum(vars))
        o.check()
        ans += o.model().eval(sum(vars)).as_long()
print(ans)