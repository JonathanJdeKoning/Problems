from collections import deque
N = int(input())
A = list(map(int, input().split()))
P = 0

K = deque([0,0,0,0])


for num in A:
    K[0] += 1
    t = sum(K)

    for _ in range(num):
        K.appendleft(0)
        K.pop()
    P += t - sum(K)
print(P)
