N = int(input())
S = input()
best = 0
for i in range(N):
    a = S[:i]
    b = S[i:]
    A = set(list(a))
    B = set(list(b))
    best = max(best, len(A.intersection(B)))
print(best)
