s = list(input())
n = int(input())

from itertools import product

k = list(product(s, repeat=2))
print("".join(k[n-1]))
