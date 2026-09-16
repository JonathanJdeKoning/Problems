input()
A = list(map(int, input().replace(","," ").split()))
A.sort()
print(A[-1] - A[0])