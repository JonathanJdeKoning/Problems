N, M , X, Y = list(map(int, input().split()))
A = list(map(int, input().split()))

B = list(map(int, input().split()))
A.sort()
B.sort()
mn = A[-1]
mx = B[0]
for i in range(X, Y):
    if X < i and i <= Y and mn < i and mx >= i:
        exit(print("No War"))
print("War")