N = int(input())
A = ["psst"]
for i in range(N):
    A.append(input())

X, Y = input().split()
X = int(X)

if A[X] == Y:
    print("Yes")
else:
    print("No")
