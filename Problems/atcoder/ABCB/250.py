A, B, C = list(map(int, input().split()))

mat = []
for i in range(A):
    row = []
    for j in range(A):
        if (i+j) %2 == 0 :
            row.append("."*C)
        else:
            row.append("#"*C)

    for _ in range(B):
        mat.append(row)
for row in mat:
    print("".join(row))