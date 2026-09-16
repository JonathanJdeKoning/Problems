N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A = [x for x in A if x != X]
print(*A)