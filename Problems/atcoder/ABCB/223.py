from collections import deque

S = input()
q = deque(list(S))

mn = list(q)
mx = list(q)

for _ in range(len(S)):
    q.rotate(1)
    mn = min(mn, list(q))
    mx = max(mx, list(q))

print("".join(mn))
print("".join(mx))