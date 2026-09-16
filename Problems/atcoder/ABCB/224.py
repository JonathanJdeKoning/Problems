R, C = list(map(int, input().split()))

mat = [list(map(int, input().split())) for _ in range(R)]


for i1 in range(R-1):
    for i2 in range(i1+1, R):
        for j1 in range(C-1):
            for j2 in range(j1+1, C):
                if mat[i1][j1] + mat[i2][j2] > mat[i2][j1] + mat[i1][j2]:
                    exit(print("No"))
print("Yes")