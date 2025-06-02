N, M = map(int, input().split())
mat = []
for _ in range(N): mat.append(list(input()))
temp = []
for _ in range(M): temp.append(list(input()))

for i in range(N - M + 1):
    for j in range(N - M + 1):
        good = True
        for k in range(M):
            for l in range(M):
                if mat[i+k][j+l] != temp[k][l]:
                    good = False
        if good: exit(print("Yes"))
print("No")



