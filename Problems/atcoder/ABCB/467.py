N = int(input())
X = 0
Y = 0
for _ in range(N):
    A, B, S = input().split()
    A, B = int(A), int(B)
    Y += B - A
    if S == "take":
        X += B - A
print(Y - X)
    
