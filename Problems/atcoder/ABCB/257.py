N, K , Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for op in L:
    op -= 1
    if op == len(A)-1:
        if A[op] == N: continue
    else:
        if A[op+1] == A[op]+1: continue
    A[op] += 1

print(" ".join(map(str, A)))
