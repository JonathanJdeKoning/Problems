from collections import defaultdict, deque
N = int(input())

edges = defaultdict(list)

ceos = []
for i in range(1, N+1):
    n = int(input())
    if n == -1:
        ceos.append(i)
    if n != -1:
        edges[n].append(i)

ans = 0
for node in ceos:
    levels = 0 
    q = deque([node])
    while q:
        levels += 1
        for _ in range(len(q)):
            curr = q.popleft()

            for neighbor in edges[curr]:
                q.append(neighbor)

    ans = max(ans, levels)
print(ans)

