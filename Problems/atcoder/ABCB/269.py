M= []
for _ in range(10):
    M.append(input())

A, B, C, D = -1, -1, -1, -1

for i in range(10):
    for j in range(10):
        if M[i][j] == ".": continue
        if A == -1: A = i+1
        if C == -1: C = j+1
        B = i+1
        D = j+1
print(A, B)
print(C, D)
