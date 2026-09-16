N, M = list(map(int, input().split()))
mat = []
seen = set()
for _ in range(N):
    mat.append(list(input()))


for i in range(N - M + 1):
    for j in range(N - M +1):
        box = []

        for k in range(i, i+M):
            for l in range(j, j+M):
                box.append(mat[k][l])
        seen.add("".join(box))

print(len(seen))

