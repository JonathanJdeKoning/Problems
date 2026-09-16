def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = [A, B]
    ops = 0

    loc = {}
    for i in range(2):
        for j in range(N):
            loc[M[i][j]] = (i,j)
    ey = 0
    ex = 0
    ans = []
    for num in range(1, 2*N+1):
        while loc[num] != (ey, ex):
            ops += 1
            y, x= loc[num]
            if x != ex:
                if ex < x:
                    loc[num], loc[M[y][x-1]]      = loc[M[y][x-1]],      loc[num]
                    M[y][x], M[y][x-1] = M[y][x-1], M[y][x]
                    ans.append((1+y, x))
                else:
                    loc[num], loc[M[y][x+1]]      = loc[M[y][x+1]],      loc[num]
                    M[y][x], M[y][x+1] = M[y][x+1], M[y][x]
                    ans.append((1+y, x+1))
                continue
            if y != ey:
                loc[num], loc[M[abs(y-1)][x]] = loc[M[abs(y-1)][x]], loc[num]
                M[y][x], M[abs(y-1)][x] = M[abs(y-1)][x], M[y][x]
                ans.append((3, x+1))
                continue

        ex += 1
        if ex == N:
            ey += 1
            ex = 0
        
    print(ops)
    for op, idx in ans:
        print(op, idx)

for _ in range(int(input())):
    solve()