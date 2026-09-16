from math import ceil, floor

N = input()
M = len(N)
N = int(N)

N -= N%10

N //= 10
print(N)