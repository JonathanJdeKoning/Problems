from collections import defaultdict
from functools import cache
ans = 0
parents = defaultdict(list)
with open("data.in","r") as file:
    for line in file.readlines():
        l = line.strip().split()
        u = l[0][:-1]
        for v in l[1:]:
            parents[v].append(u)

memo = {}
def numWays(node, dac, fft):
    if (node, dac, fft) in memo:
        return memo[(node, dac, fft)]
    if node == "svr":
        if dac and fft: return 1
        return 0
    if node == "dac":
        dac = True
    if node == "fft":
        fft = True
    ans = sum([numWays(p, dac, fft) for p in parents[node]])
    memo[(node,dac,fft)] = ans
    return ans
print(numWays("out", False, False))