from itertools import groupby
N = int(input())

A = [len(set(input().split())) == 1 for _ in range(N)]
for k,v in groupby(A):
    if len(list(v)) >=3 and k : exit(print("Yes"))
print("No")
