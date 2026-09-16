from math import dist
X, Y = map(int, input().split())

high = 1 # good
low = 0 # bad
for _ in range(100):
    M = (low+high) / 2
    if dist((X*M, Y*M), (0,0)) >= 1:
        high = M
    else:
        low = M

print(X*M, Y*M)
