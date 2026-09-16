from collections import defaultdict
N = int(input())

A = list(map(int, input().split()))
mp = defaultdict(int)
for num in A:
    mp[num] += 1

for k in mp:
    if mp[k] == 3:
        exit(print(k)) 