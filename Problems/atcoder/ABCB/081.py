from math import log2
N = int(input())
A = list(map(int, input().replace(","," ").split()))
print(min([int(log2(num&(-num))) for num in A]))