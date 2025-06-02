from collections import defaultdict
N,M = map(int, input().split())
mp = defaultdict(int) 
for _ in range(M):
    a, b= map(int, input().split())
    mp[a] += 1
    mp[b] += 1

for i in range(1, N+1):
    print(mp[i])

