N = int(input())

A = list(map(int, input().split()))
good = sorted(A)
for i in range(len(A) - 1):
    for j in range(len(A)):
        A[i], A[j] = A[j], A[i]
        if A == good:
            exit(print("YES"))
        A[i], A[j] = A[j], A[i]

print("NO")