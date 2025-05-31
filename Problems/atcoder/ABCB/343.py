n = int(input())
mat = [map(int, input().split()) for _ in range(n)]

for i, row in enumerate(mat):
    out = []
    for j, cell in enumerate(row, start=1):
        if cell:
            out.append(j)

    print(" ".join(map(str, out)))
