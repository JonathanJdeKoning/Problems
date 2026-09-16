N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

p = sum(A)
for i in range(1, len(A), 2):
    p -= 1

if p <= X:
    print("Yes")
else:
    print("No")