N = int(input())
A = list(map(int, input().split()))

T = sum(A)
sub = 0
best = int(1e9)
for i in range(len(A)):
    sub += A[i]
    best = min(best, abs((T-sub) -  sub))

print(best)