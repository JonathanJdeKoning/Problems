poss = [
    [
        [1,1],
        [1,1]
    ],
     
    [
        [1,1,1,1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],

    [
        [0,1,0],
        [1,1,1]
    ],
    [
        [1,0],
        [1,1],
        [1,0]
    ],
    [
        [1,0,0],
        [1,1,1]
    ],
    [
        [1,1],
        [1,0],
        [1,0]
    ],
    [
        [1,0],
        [1,1],
        [0,1]
    ],
    [
        [0,1,1],
        [1,1,0]
    ]
]

rows, cols = list(map(int, input().split()))
M = [list(map(int, input().split())) for _ in range(rows)]

ans = 0
for tetA in poss:
    H, W = len(tetA), len(tetA[0])
    tetB = [row[::-1] for row in tetA]
    tetC = tetA[::-1]
    tetD = [row[::-1] for row in tetC]
    for i in range(rows-H+1):
        for j in range(cols-W+1):
            A = 0
            B = 0
            C = 0
            D = 0
            for ii in range(H):
                for jj in range(W):
                    A += M[i+ii][j+jj]*tetA[ii][jj]
                    B += M[i+ii][j+jj]*tetB[ii][jj]
                    C += M[i+ii][j+jj]*tetC[ii][jj]
                    D += M[i+ii][j+jj]*tetD[ii][jj]
            ans = max(ans, A,B,C,D)
print(ans)

    
