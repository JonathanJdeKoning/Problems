from collections import deque
q = deque(list(input()))
t = 0
for _ in range(3):
    q.rotate(1)
    t += int("".join(q))
print(t)

