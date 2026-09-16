from collections import defaultdict
N = int(input())
mp = defaultdict(int)
for _ in range(N):
    mp[input()] += 1

mx = max(list(mp.values()))
for k in mp:
    if mp[k] == mx: exit(print(k))
    
