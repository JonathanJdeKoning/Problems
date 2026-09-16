A, B, K = list(map(int, input().split()))


a = min(A, K)
A -= a
K -= a

if K ==0: exit(print(A, B))

b = min(B, K)

B -= b

print(A,B)