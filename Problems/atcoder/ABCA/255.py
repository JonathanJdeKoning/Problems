mat = []

n,m = map(int, input().split())
for _ in range(2):
    mat.append(list(map(int, input().split())))

print(mat[n-1][m-1])
