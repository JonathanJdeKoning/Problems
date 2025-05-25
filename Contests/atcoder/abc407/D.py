R, C = list(map(int, input().replace(","," ").split()))

mat = [list(map(int, input().split())) for _ in range(R)]

ans = 0
for row in mat:
    for cell in row:
        ans ^= cell

score = ans  
dominoed = set()

def nextTile(i,j):
    if i == R-1 and j == C-1: return (-1,-1)

    if j != C - 1:
        return (i, j+1)
    return (i+1, 0)

def backtrack(i,j):
    global score
    global ans

    if (i,j) == (-1,-1):
        ans = max(score, ans)
        return

    if (i,j) in dominoed:
        backtrack(*nextTile(i,j))
        return

    backtrack(*nextTile(i,j))

    if i < R-1 and (i+1, j) not in dominoed:
        score ^= mat[i][j]
        score ^= mat[i+1][j]

        dominoed.add((i,j))
        dominoed.add((i+1,j))

        backtrack(*nextTile(i,j))

        score ^= mat[i][j]
        score ^= mat[i+1][j]

        dominoed.discard((i,j))
        dominoed.discard((i+1,j))



    if j < C-1 and (i, j+1) not in dominoed:
        score ^= mat[i][j]
        score ^= mat[i][j+1]

        dominoed.add((i,j))
        dominoed.add((i,j+1))

        backtrack(*nextTile(i,j))

        score ^= mat[i][j]
        score ^= mat[i][j+1]
        
        dominoed.discard((i,j))
        dominoed.discard((i,j+1))


backtrack(0,0)
print(ans)