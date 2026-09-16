from math import ceil
N , D = list(map(int, input().split()))

V = 2*D+ 1

print(ceil(N / V))
