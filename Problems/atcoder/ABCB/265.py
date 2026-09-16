N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonus = []
for _ in range(M):
    X, Y= map(int, input().split())
    bonus.append((X, Y))
bonus = bonus[::-1]
for i, room in enumerate(A, start =1):
    if bonus and bonus[-1][0] == i:
        T += bonus.pop()[1]
    if T > room:
        T -= room
    else:
        exit(print("No"))
print("Yes")
