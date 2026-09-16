N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

votes = sum(A)

if len([x for x in A if x >= votes * (1/(4*M))]) >= M:
    print("Yes")
else:
    print("No")