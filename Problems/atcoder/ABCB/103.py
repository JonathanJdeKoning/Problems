from collections import deque
S = deque(list(input()))
T = deque(list(input()))


for _ in range(102):
    if S == T:
        exit(print("Yes"))
    S.rotate(1)
print("No")
