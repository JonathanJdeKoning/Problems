from collections import defaultdict
N, M = map(int, input().split())

mp = defaultdict(int)

for _ in range(N):
    C, S = map(int, input().split())
    mp[C] = max(mp[C], S)


A = []
for i in range(1, M+1):
    if i not in mp:
        A.append(-1)
    else:
        A.append(mp[i])

print(" ".join(map(str, A)))

    
