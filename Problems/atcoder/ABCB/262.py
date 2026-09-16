from collections import defaultdict
N, M = map(int, input().split())
E = {i:set() for i in range(1, N+1)}

for _ in range(M):
    U, V = map(int, input().split())

    E[U].add(V)
    E[V].add(U)
ans = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            if j in E[i] and k in E[j] and i in E[k]:
                ans += 1
print(ans)





