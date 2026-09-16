from collections import defaultdict
N = int(input())
mp = defaultdict(list)
for i in range(N):
    s, t = input().split()
    mp[i] = [s,t]


for k,v in mp.items():
    good1 = True
    good2 = True
    for kk, vv in mp.items():
        if kk == k: continue
        if vv[0] == v[0] or vv[1] == v[0]:
            good1 = False
        if vv[0] == v[1] or vv[1] == v[1]:
            good2 = False

    if not good1 and not good2:
        exit(print("No"))



print("Yes")
