from math import dist
N = int(input())
A = list(map(int, input().split()))
print(sum([abs(x) for x in A]))
print(dist(tuple(A), (0,)*N))
print(max([abs(x) for x in A]))