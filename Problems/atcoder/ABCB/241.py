from collections import Counter
N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

fq = Counter(A)
B = list(map(int, input().split()))


for x in B:
    if fq[x] >= 1:
        fq[x] -= 1
    else:
        exit(print("No"))
print("Yes")