N, X = list(map(int, input().split()))
X -= 1
A = list(map(int, input().split()))

seen = set([X])

while True:
    X = A[X] - 1
    if X in seen: break
    seen.add(X)
print(len(seen))