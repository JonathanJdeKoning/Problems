from itertools import permutations, combinations

nums = list(range(1,11))


poss = []
for p in permutations(nums, 3):
    if sum(p) == 14:
        poss.append(p)
good = set([1,2,3,4,5,6,7,8,9,10])
solutions = set()
curr = []
def solve(p,left):
    curr.append(p)
    if left == 0:
        solutions.add(toString(curr.copy()))
        curr.pop()
        return
    
    good.discard(p[0])
    good.discard(p[1])

    if left == 1:
        for np in poss:
            if np[0] not in good: continue
            if np[1] != p[2]: continue
            if np[2] != curr[0][1]: continue
            solve(np, 0)
    else:     
        for np in poss:
            if np[0] not in good: continue
            if np[2] not in good: continue
            if np[1] != p[2]: continue
            good.discard(np[1])
            solve(np, left-1)
            good.add(np[1])
            
    curr.pop()
    good.add(p[0])
    good.add(p[1])

for p in poss:
    solve(p, 4)

def toString(sol):
    r = [s[0] for s in sol]
    m = min(r)
    x = r.index(m)
    ans = []

    for t in sol[x:]:
        ans.append(str(t[0]))
        ans.append(str(t[1]))
        ans.append(str(t[2]))

    for t in sol[:x]:
        ans.append(str(t[0]))
        ans.append(str(t[1]))
        ans.append(str(t[2]))

    f = "".join(ans)
    if len(f) == 17: return "0"
    return f

print(max(solutions))
    
