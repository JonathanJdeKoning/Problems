from itertools import groupby
T = int(input())
def solve():
    N = int(input())
    S = input()

    g = []
    for k,v in groupby(S):
        g.append((k, len(list(v)))
                 )
    if g[0][0] == '0': g = g[1:]
    if len(g) <= 1: return 0
    if g[-1][0] == '0': g.pop()
    if len(g) <= 1: return 0
    

    print(g)

for _ in range(T):
    print(solve())