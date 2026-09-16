N, K = list(map(int, input().split()))

A = list(map(int, input().split()))
A.sort()
print(sum(A[:K]))