N , S , D = list(map(int, input().split()))

for _ in range(N):
    s , d = list(map(int, input().split()))
    if s < S and d > D : exit(print("Yes"))

print("No")