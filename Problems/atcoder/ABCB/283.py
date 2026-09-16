N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1: A[op[1]-1] = op[2]
    else: print(A[op[1]-1])

