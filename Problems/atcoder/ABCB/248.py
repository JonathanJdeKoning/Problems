from math import log
A, B, K = list(map(int, input().split()))


for i in range(10000000):
    if A >= B: break
    A *= K

print(i)

