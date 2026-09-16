from math import inf
N = int(input())
best = inf
A = []
for _ in range(N):
    a,b = list(map(int, input().split()))
    A.append((a,b))

for i in range(len(A)):
    a,b = A[i]
    for j in range(i, len(A)):
        x, y= A[j]

        if j == i:
            best = min(best, a+b)
        else:
            best = min(best, min(max(a,y), max(b,x)))

print(best)

    
