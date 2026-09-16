from math import comb


N = int(input())

for i in range(1,N+1):
    row = []
    for j in range(i):
        row.append(comb(i-1,j))
    print(*row)