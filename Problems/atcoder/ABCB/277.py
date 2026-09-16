from itertools import pairwise
N = int(input())
A = []
for _ in range(N):
    A.append(input())

goodFirst = "HDSC"
goodLast="A23456789TJQK"

if not all(x[0] in goodFirst and x[1] in goodLast for x in A): exit(print("No"))
if len(set(A)) != len(A): exit(print("No"))
print("Yes")
